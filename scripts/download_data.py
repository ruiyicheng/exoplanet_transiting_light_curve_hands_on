#!/usr/bin/env python3

from pathlib import Path

from huggingface_hub import snapshot_download


DATASET_REPO_ID = "ruiyicheng/exoplanet_transiting_light_curve_hands_on-data"
REPO_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = REPO_ROOT / "input"


def main() -> None:
    snapshot_download(
        repo_id=DATASET_REPO_ID,
        repo_type="dataset",
        local_dir=INPUT_DIR,
        allow_patterns=[
            "bias/*",
            "flat/*",
            "mid_transit_time/*",
            "science_image/*",
        ],
    )
    (INPUT_DIR / "light_curve").mkdir(parents=True, exist_ok=True)
    print(f"Downloaded dataset into {INPUT_DIR}")
    print(
        "Create input/light_curve/light_curve.csv yourself with AstroImageJ "
        "before running Light_curve_fitting.ipynb."
    )


if __name__ == "__main__":
    main()
