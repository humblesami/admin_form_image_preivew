from setuptools import find_namespace_packages, setup
import distutils.errors

bdist_wheel = None

try:
    import wheel.bdist_wheel
    class bdist_wheel(wheel.bdist_wheel.bdist_wheel):
        def run(self, *args, **kwargs):
            raise distutils.errors.DistutilsClassError("Error raised")
except ModuleNotFoundError:
    pass

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='admin-form-image-preivew',
    version='1.2',
    description='Test package.',
    # cmdclass={'bdist_wheel': bdist_wheel},
    # package_dir={'': 'src'},
    # packages = find_packages(where="src"),
    packages=find_namespace_packages(
        include=[
            "app1.templates.admin",
            "app1",
        ],
    ),
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
    url="https://github.com/humblesami/admin_form_image_preivew.git",
    install_requires=['Django'],
    # keywords='git tag git-tagup tagup tag-up version autotag auto-tag commit message',
    # project_urls={'Homepage': 'https://initialcommit.com/tools/git-tagup',},
    # entry_points={ 'console_scripts': [ 'git-tagup=git_tagup.__main__:main','gtu=git_tagup.__main__:main',],}
)