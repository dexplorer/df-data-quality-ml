import setuptools

setuptools.setup(
    name="dqml_app",
    version="1.0.2",
    scripts=["./scripts/dqml_app"],
    author="Rajakumaran Arivumani",
    description="Data quality ml app install.",
    url="https://github.com/dexplorer/df-data-quality-ml",
    packages=[
        "dqml_app",
        "dqml_app.data_sample",
        "dqml_app.feature_eng",
        "dqml_app.explainability",
    ],
    # packages = find_packages(),
    install_requires=[
        "setuptools",
        "requests",
        "utils@git+https://github.com/dexplorer/utils#egg=utils-1.0.1",
        "metadata@git+https://github.com/dexplorer/df-metadata#egg=metadata-1.0.6",
        "app_calendar@git+https://github.com/dexplorer/df-app-calendar#egg=app_calendar-1.0.2",
    ],
    python_requires=">=3.12",
)
