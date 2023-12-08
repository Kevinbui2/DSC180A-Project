# Streetwatch: Utility and Wildfire Risks Detected From Street View Imagery

San Diego Gas & Electric leverages many different public and private data sources to make critical decisions that impact our communities. We would like to explore Google Street View as a publicly available source of data to help us identify risks that can be observed from the perspective of San Diego citizens. The project goals are to quantify the ability to observe damaged assets or fire from commonly traveled paths, determine whether there are clear compliance infractions that can be seen from the citizen's perspective, and identify other utility-related hazards that can be seen from this public data source. In this case, we
will be using [DETR](https://github.com/facebookresearch/detr) to detect poles and surface structures.
 
## Data Sources
Data for this project is collected from [Google Street View Static API](https://developers.google.com/maps/documentation/streetview/overview). 

You must add `images` folder from [Streetview Repo](https://github.com/pdashk/streetwatch) to root directory to be able to create the training and validation set.

## Setup

### Conda Environment
After cloning repo, navigating to root level and run:
```
conda env create -f environment.yml
```

### Detr Model
You must clone the detr repo to be able to train the mode:
```
git clone https://github.com/woctezuma/detr.git
cd detr/
git checkout finetune
cd ..
```

### Create Training and Validation Sets
After adding `images` folder to root directory, run:
```
python scripts/train_validate_split.py
```
After this is ran, 2 new folders will be created in data/custom/ which are `train2017` and `val2017`.

### Fine-tuning model
Run `detr_main.ipynb` to fine-tune DETR on the streeview dataset.

# Project Structure

```
├── data/custom/        <- Local data files only (do not commit)
│   ├── annotations
│   ├── train2017
│   ├── val2017
│
├── detr/               <- Cloned detr repo (do not commit)
│
├── detr_main.ipynb     <- Python notebook to train model
│
├── scripts             <- Python scripts to run in command line 
│   ├── train_validate_split.py
│
├── outputs             <- Location of model after fine-tuning and log (do not commit local model)
│
├── .gitignore          <- Git ignore file
│
├── environment.yml     <- Conda environment file
│
└── README.md           <- The top-level README for repo
```

path/to/coco/
├ annotations/  # JSON annotations
│  ├ annotations/custom_train.json
│  └ annotations/custom_val.json
├ train2017/    # training images
└ val2017/      # validation images