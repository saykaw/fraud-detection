# Credit Card Fraud Detection on Highly Imbalanced Dataset.

Follow the steps.

## Prerequisites

- Python 3.6 or higher
- Node

## Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/dyo-tak/ml-fraud-detection
```

## Starting Frontend

Change directory to ./frontend and install dependencies 

```bash
cd ./frontend
pnpm install
pnpm run dev
```

## Starting Backend Server

Change directory to ./backend, create python environment and then install dependencies 

```bash
cd ./backend
python3 -m venv .venv
pip3 install -r requirements.txt
flask run
```

## Dataset

Download the dataset from [link](https://www.kaggle.com/datasets/kartik2112/fraud-detection) and add the fraudTrain.csv, fraudTest.csv to the directory backend/data.
