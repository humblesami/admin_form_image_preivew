import os
from setuptools import find_namespace_packages, setup


install_requires = [
    "django",
]

test_requires = [
    "tox",
    "tox-gh-actions",
    "pluggy>=0.7",
    "mock",
    "unittest-xml-reporting",
    "codacy-coverage",
    "django-migration-fixer",
]

deploy_requires = [
    "bump2version",
    "readme_renderer[md]",
    "git-changelog",
]


local_dev_requires = [
    "pip-tools",
    "check-manifest",
]

extras_require = {
    "development": [
        local_dev_requires,
        install_requires,
        test_requires,
        deploy_requires,
    ],
    "test": test_requires,
    "deploy": deploy_requires,
}

BASE_DIR = os.path.dirname(__file__)
README_PATH = os.path.join(BASE_DIR, "README.md")
LONG_DESCRIPTION_TYPE = "text/markdown"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='admin-form-image-preivew',
    version='1.3',
    description='Test package.',
    # cmdclass={'bdist_wheel': bdist_wheel},
    # package_dir={'': 'src'},
    # packages = find_packages(where="src"),

    # packages = find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sami Akram",
    author_email="samiakram@live.com",
    url="https://github.com/humblesami/admin_form_image_preivew.git",

    include_package_data=True,
    python_requires=">=3.6",
    install_requires=install_requires,
    tests_require=["coverage"],
    extras_require=extras_require,
    packages=find_namespace_packages(
        include=[
            "app1.templates.admin",
            "app1"
        ],
    ),
)