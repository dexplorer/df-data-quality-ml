import setuptools

setuptools.setup(
    name="dqml_app",
    version="1.0.1",
    scripts=["./scripts/dqml_app"],
    author="Rajakumaran Arivumani",
    description="Data quality ml app install.",
    url="https://github.com/dexplorer/df-data-quality-ml",
    packages=[
        "dqml_app",
        "dqml_app.data_sample",
        "dqml_app.feature_eng",
        "dqml_app.explainability",
        "dqml_app.app_calendar",
    ],
    # packages = find_packages(),
    install_requires=[
        "setuptools",
        "requests", 
        "utils@git+https://github.com/dexplorer/utils#egg=utils-1.0.1",
        "metadata@git+https://github.com/dexplorer/df-metadata#egg=metadata-1.0.3",
    ],
    python_requires=">=3.12",
)
