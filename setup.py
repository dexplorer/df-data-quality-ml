import setuptools

setuptools.setup(
    name="dqml_app",
    version="1.0",
    scripts=["./scripts/dqml_app"],
    author="Me",
    description="Data quality ml app install.",
    packages=[
        "dqml_app",
        "dqml_app.utils",
        "dqml_app.data_sample",
        "dqml_app.feature_eng",
        "dqml_app.explainability",
    ],
    # packages = find_packages(),
    install_requires=[
        "setuptools",
    ],
    python_requires=">=3.12",
)
