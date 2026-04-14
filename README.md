# 2025 Exoplanet Hands-On

This repository contains the notebooks and reference material for a hands-on exercise on calibrating images of the transiting exoplanet WASP-11b and fitting its light curve.

## Reading order

1. `prerequisites.pdf`
2. `Calibrate.ipynb`
3. `Guide_for_AstroimageJ.pdf`
4. `Light_curve_fitting.ipynb`

## Data location

The raw and auxiliary data are stored separately from the code in the Hugging Face dataset repository:

`https://huggingface.co/datasets/ruiyicheng/exoplanet_transiting_light_curve_hands_on-data`

The notebooks in this GitHub repo expect the downloaded files to live under `./input/`.

## How to obtain the data

Recommended method:

```bash
pip install huggingface_hub
python scripts/download_data.py
```

This downloads the dataset into `./input/` with the directory layout expected by the notebooks:

```text
input/
├── bias/
├── flat/
├── mid_transit_time/
└── science_image/
```

Manual CLI alternative:

```bash
hf download ruiyicheng/exoplanet_transiting_light_curve_hands_on-data \
  --repo-type dataset \
  --local-dir input
```

## Generate `light_curve.csv` yourself

The dataset repo contains the calibration frames, science images, and mid-transit timing tables. It does not contain `input/light_curve/light_curve.csv`.

Students should generate that file themselves in AstroImageJ by following `Guide_for_AstroimageJ.pdf`, then save it at:

```text
input/light_curve/light_curve.csv
```

If `input/light_curve/` does not exist yet, create it locally before saving the CSV.

`Light_curve_fitting.ipynb` expects that CSV to exist.

## Things to explore

1. Collect your own transiting-exoplanet data using Muguang Observatory.
2. Find a variable star in the dataset and show its light curve.

Hint: search for variable stars in the vicinity of this field using the Gaia archive (ADQL). EW-type stars should be visible.

3. Try PSF photometry.
4. Try to extract the light curve of all stars in the image.

Hint: you will need your own software for light-curve extraction. `sep` is a useful package for this.

5. Resolve the WCS of the image and cross-match it with the Gaia catalog.
6. Check whether there are any unknown variable sources in the dataset.

If you find something interesting, contact `ruiyicheng@sjtu.edu.cn`.
