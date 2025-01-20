import setuptools

setuptools.setup(
    name="dqml_app",
    version="1.0.0",
    scripts=["./scripts/dqml_app"],
    author="Me",
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
        'utils@git+https://github.com/dexplorer/utils#egg=utils-1.0.0',
    ],
    python_requires=">=3.12",
)
