mlops-mini-project
==============================
This is an **end-to-end Machine Learning project with MLOps best practices**. It demonstrates how to build a reproducible, maintainable, and deployable ML pipeline using modern MLOps tools and workflows.

## Project Overview

The project goes beyond just training a machine learning model — it incorporates **data versioning, experiment tracking, modular code, and deployment automation**. It is structured to simulate a production-level ML workflow.

Key highlights:

* **Data Versioning:** Uses **DVC (Data Version Control)** to track datasets and intermediate processing steps, ensuring reproducibility.
* **Modular Code Structure:** Organized into `src/` folders for data processing, feature engineering, model training, prediction, and visualization.
* **Experiment Tracking:** Uses **MLflow** to log experiments, track metrics, parameters, and models for reproducibility.
* **Automated Testing:** Includes unit tests in `tests/` and environment checks using `tox.ini`.
* **CI/CD Automation:** GitHub Actions workflow automates testing and pipeline execution.
* **Deployment:** Containerized with **Docker** and includes a **Flask API** for serving predictions.
* **Configuration Management:** Parameters are centralized in `params.yaml` for easy experimentation.
* **Documentation:** Includes `notebooks/` for exploratory analysis, `reports/` for model results, and `docs/` for project documentation.

## Project Structure

```
├── data/             # Raw, interim, and processed datasets
├── src/              # Source code
│   ├── data/         # Scripts for data fetching/creation
│   ├── features/     # Feature engineering scripts
│   ├── models/       # Model training and prediction scripts
│   └── visualization/# Data visualization scripts
├── tests/            # Unit tests
├── flask_app/        # Flask API for model serving
├── mlruns/           # MLflow experiment logs
├── params.yaml       # Pipeline parameters
├── requirements.txt  # Python dependencies
├── Dockerfile        # Containerization
└── Makefile          # Pipeline automation
```

## Tools & Technologies

* **Python** – for scripting and ML development
* **Scikit-Learn** – for ML modeling
* **DVC** – for data version control
* **MLflow** – for experiment tracking and model registry
* **Docker** – for containerization
* **Flask** – for serving model predictions
* **GitHub Actions** – for CI/CD automation

## Key Learning Outcomes

By studying and running this project, you will learn how to:

* Build **reproducible ML pipelines**
* Track **data, experiments, and models** efficiently
* Structure a project in a **production-ready way**
* Deploy a model using **Docker and Flask**
* Automate tasks using **Makefile and GitHub Actions**

---



<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
