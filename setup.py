from setuptools import setup, find_packages


setup(
    name="taggy",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["PyGObject"],
    include_package_data=True,
    entry_points={
        "gui_scripts": [
            "taggy = taggy.gui.__main__:run"
        ]
    }
)
