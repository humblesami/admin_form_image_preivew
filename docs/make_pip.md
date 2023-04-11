**Make PIP your self**

1. `git clone https://github.com/humblesami/admin_form_image_preivew.git`
2. `cd admin_form_image_preivew`

3. Find and replace `admin_form_image_preivew` with your own `your_module_name`
4. Find and replace `admin-form-image-preivew` with your own `your-module-name`
5. Install twine
`sudo apt-get update`
`sudo apt-get install twine`

6. Make your build
6.1. rm -r dist/*
6.2. rm -r build/*
6.3. python setup.py clean --all
6.4. python setup.py sdist bdist_wheel -v=1.1

**Install and test locally**
pip uninstall admin-form-image-preivew
pip install dist/your_module_name-1.1-py3-none-any.whl


**Upload your**

https://twine.readthedocs.io/en/stable/

pip install twine

twine upload dist/*
twine upload dist/* --config-file ~/.pypirc_test
or
twine upload dist/* --config-file ~/.pypirc_prod


**Sample config files for twine**

1.
.pypirc_test

[distutils]
index-servers = pypi

[pypi]
repository: https://test.pypi.org/legacy/
username: __token__
password: token1



*Install the uploaded package*
pip install -i https://test.pypi.org/simple/ admin-form-image-preivew

================================================================

2.
.pypirc_prod

[distutils]
index-servers = pypi

[pypi]
repository: https://pypi.org/legacy/
username: __token__
password: token2

*Install the uploaded package*
pip install admin-form-image-preivew