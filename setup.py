import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='admin_form_image_preivew',
    version='0.0.23',
    description='Test package.',
    py_modules=["admin_form_image_preivew"],
    package_dir={'': 'src'},
    packages = setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sami Akram",
    author_email="samiakram@live.com",
    url="https://github.com/humblesami/admin_form_image_preivew",
    # install_requires=['gitpython'],
    # keywords='git tag git-tagup tagup tag-up version autotag auto-tag commit message',
    # project_urls={'Homepage': 'https://initialcommit.com/tools/git-tagup',},
    # entry_points={ 'console_scripts': [ 'git-tagup=git_tagup.__main__:main','gtu=git_tagup.__main__:main',],}
)