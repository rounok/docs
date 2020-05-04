# module to packaage
sample_package

## Steps to create sample_package and upload to pypi

### Prerequsites
* Python3.6
* docker
* Accounts created in test.pypi.org and pypi.org 

## have following files created for your project:


### Get required files to include in library
1. copy needed files to dir

4. Update VERSION file with the required value

### Create Linux wheel file
1. Pull the manylinux docker image and run it
  ```
  $ docker pull quay.io/pypa/manylinux2010_x86_64
  $ docker images
  $ docker run -it <image_id>
  ```
  This will open a interactive session with the docker container
2. In a separate terminal copy project dir in project root to the above docker container
  ```
  $ docker cp package_folder <container-id>:/
  ```
3. Go to package_folder directory in the docker container using the interactive session opened in step1
4. Create virtual environement and install required libraries inside docker container
  ```
  $ /opt/python/cp36-cp36m/bin/python -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements_dev.txt
  ```
5. Create Linux wheel file
  ```
  $ python setup.py bdist_wheel
  ```
  Linux wheel file is created at dist/ibm_wos_utils-1.0-cp36-cp36m-linux_x86_64.whl

6. Convert linux wheel file to manylinux wheel file
  ```
  $ auditwheel repair dist/package_name-1.0-cp36-cp36m-linux_x86_64.whl -w dist
  $ rm -rf dist/package_name-1.0-cp36-cp36m-linux_x86_64.whl
  ```
  Manylinux wheel files are created at dist/package_name-1.0-cp36-cp36m-manylinux1_x86_64.whl, dist/package_name-1.0-cp36-cp36m-manylinux2010_x86_64.whl
  
7. Copy the wheel files from docker container to local system
  ```
  $ docker cp <container-id>:/package_folder/dist api-client-utils/package_name
  ```
 
### Create MacOSX wheel file
1. Go to `package_folder` directory
2. Create virtual environement and install required libraries
  ```
  $ python3.6 -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements_dev.txt
  ```
3. Create MacOSX distribution
  ```
  $ python setup.py bdist_wheel
  ```
  Wheel file is created at dist/package_name-1.0-cp36-cp36m-macosx_10_9_x86_64.whl


### Uploading the wheel files to test pypi and pypi

After completing the above steps dist directory should have 3 files
```
package_name-1.0-cp36-cp36m-manylinux1_x86_64.whl
package_name-1.0-cp36-cp36m-manylinux2010_x86_64.whl
package_name-1.0-cp36-cp36m-macosx_10_9_x86_64.whl
```

* Uploading the library to test pypi
```
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

* Uploading the library to pypi
```
$ twine upload dist/*
```
