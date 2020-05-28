## Một vài ghi chú khi sử dụng python 

### Tạo file requiement

	pip freeze > stable-req.txt


### Cài đặt môi trường ảo

```sh
yum install python3.6 python36-pip -y
pip3 install --upgrade pip
pip  install virtualenv
mkdir env
virtualenv  env/
source env/bin/activate
pip install ipython
```