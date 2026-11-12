
### COMPUTE LUMINOSITY ###

## Written by : LJ Iain Spriggs

### Required Imports ###

import pandas as pd
import numpy as np
from dustapprox.models import PrecomputedModel
import sys
from pathlib import Path
homedir = Path.home()
sys.path.append(str(homedir)+"/"+"gaiadr3_bcg") # navigate to dir containing corr package
import gdr3bcg.bcg as bcg

### Compute G-band Extinction ###

model_library = PrecomputedModel()
r = model_library.find(passband="GAIA_GAIA3.G")
model = model_library.load_model(r[2], passband="GAIA_GAIA3.G") # r[2] corresponds to Fitzpatrick (1999)
#print("Gaia DR3 G-band Required Inputs (Fitzpatrick, 1999):", model.feature_names)

def compute_ag(a0_array, teff_array):
    # convert inputs to pd dataframe for easy manipulation
    df = pd.DataFrame({
        "a0": np.array(a0_array),
        "teff": np.array(teff_array)
    })
    # only pass valid a0 + teff
    mask = (
        np.isfinite(df["teff"]) & (df["teff"] >= 3500) & (df["teff"] <= 5e4) &
        np.isfinite(df["a0"]) & (df["a0"] >= 0.01) & (df["a0"] <= 20)
    )
    # use A_G = A_0 when a0 or teff invalid
    df["ag"] = df["a0"].copy().astype(float)
    # model compute k_G such that A_G = k_G * A_0
    if mask.any():
        in_df = pd.DataFrame({
            "A0": df.loc[mask, "a0"],
            "teffnorm": df.loc[mask, "teff"] / 5040
        })
        k_G = model.predict(in_df)
        df.loc[mask, "ag"] = k_G * df.loc[mask, "a0"]
    return np.array(df["ag"])

### Compute G-band Bolometric Correction ###

table = bcg.BolometryTable()

def compute_bc(teff_array, logg_array, feh_array):
    # convert inputs into pd dataframe for easy manipulation
    df = pd.DataFrame({
        "teff": np.array(teff_array),
        "logg": np.array(logg_array),
        "feh": np.array(feh_array)
    })
    # define single computation of BC
    def bc(teff, logg, feh):
        if np.isfinite(teff) & np.isfinite(logg) & np.isfinite(feh):
            return table.computeBc([teff, logg, feh, 0])
        else:
            return np.nan
    # create array of BC values
    df["bc"] = [bc(t, g, m) for t, g, m in zip(df["teff"], df["logg"], df["feh"])]
    return np.array(df["bc"])

### Corrected G-band Magnitudes ###

# m_G,corr = m_G,obs - A_G

def corr_mag(mg_array, ag_array):
    mcorr_array = np.array(mg_array) - np.array(ag_array)
    return np.array(mcorr_array)

### Derive Absolute Magnitudes ###

# M_G = m_G - 5*log10(d / 10pc)

def abs_mag(mcorr_array, dist_array):
    absmag_array = np.array(mcorr_array) - 5*np.log10(np.array(dist_array) / 10) # dist_array in pc
    return np.array(absmag_array)

### Apply Bolometric Correction ###

# M_bol = M_G + BC_G

def m_bol(absmag_array, bc_array):
    mbol_array = np.array(absmag_array) + np.array(bc_array)
    return np.array(mbol_array)

### Compute Luminosity ###

# L = 10^(0.4*(M_sun,bol - M_bol))*L_sun, for gdr3bcg use M_sun,bol = +4.74 = +0.08 + +4.66

def compute_lum(a0_array, teff_array, mg_array, dist_array, logg_array, feh_array):
    ag_array = compute_ag(a0_array, teff_array) # extinction
    mcorr_array = corr_mag(mg_array, ag_array) # corrected obs mag
    absmag_array = abs_mag(mcorr_array, dist_array) # abs mag
    bc_array = compute_bc(teff_array, logg_array, feh_array) # bol correction
    mbol_array = m_bol(absmag_array, bc_array) # bol mag
    lum_array = 10**(0.4*(4.74 - mbol_array)) # lum in L_sun
    df = pd.DataFrame({
        "A_0": np.array(a0_array),
        "Teff": np.array(teff_array),
        "A_G": np.array(ag_array),
        "m_G": np.array(mg_array),
        "M_corr": np.array(mcorr_array),
        "dist": np.array(dist_array),
        "M_G": np.array(absmag_array),
        "logg": np.array(logg_array),
        "FeH": np.array(feh_array),
        "BC": np.array(bc_array),
        "M_bol": np.array(mbol_array),
        "lum": np.array(lum_array)
    })
    df.to_csv("./compute_luminosity_data.csv", index=False)
    return lum_array


## testing ##
teff = [5000, 5500]
a0 = [1, 2]
logg = [1.2, 1.4]
feh = [-0.8, 0]
gmag = [13, 12]
dist = [400, 500]
print(compute_ag(a0, teff))
print(compute_bc(teff, logg, feh))
l = compute_lum(a0, teff, gmag, dist, logg, feh)
print(l)



