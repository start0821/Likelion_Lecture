# Likelion_Lecture
###강의 소스코드입니다 

처음 부분은 가상환경을 만들고 Django를 설치하는 과정이니 이미 설치되어있는 분은 넘기셔도 됩니다.

## Git Bash
```
$ pip install virtualenv
$ virtualenv env
$ source env/Scripts/activate
$ pip install django==2.1
```

## Window cmd
```
$ pip install virtualenv
$ virtualenv env
$ ./env/Scripts/activate
$ pip install django==2.1
```

장고와 가상환경 세팅이 되어있는 분들은 여기부터 실행하지면 됩니다.

```
$ git clone https://github.com/start0821/Likelion_Lecture
$ cd Likelion_Lecture
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

오류나 문의할 점 있으면 start0821@likelion.org로 연락주세요
재밌게 코딩하세요!!
