# Python_Dir_Test
Python Project Directory Structure
---
### 파일 설명
**README.md**

설명 등을 기록하는 파일, Markdown 이용, 현재 보고있는 파일

**requirements.txt**

프로그램에 이용되는 dependency 라이브러리 정의, 패키지명==버전 으로 정의하며, setup.py 에서 사용
pip 명령어를 통해 정의된 라이브러리들을 한번에 설치할 수 있음
```
$pip install -r requirements.txt
```

**setup.py**

프로젝트 최상위에서, 프로젝트의 테스트, 빌드, 배포에 필요한 정보 정의
setuptools 패키지를 사용하여 다음 명령어로 설치
```
$pip install setuptools
```



### 개요
Python 프로젝트를 위한 기본 프로젝트 코드 구조 구성


### files

 * [sample](./sample)
   * [\_\_init\_\_.py](./sample/__init__.py)
   * [module1.py](./sample/module1.py)
   * [module2.py](./sample/module2.py)
   * [sample.py](./sample/sample.py)
 * [tests](./tests)
   * [\_\_init\_\_.py](./tests/__init__.py)
   * [test_module1.py](./tests/test_module1.py)
   * [test_module2.py](./tests/test_module2.py)
 * [docs](./docs)
   * [README.md](./docs/README.md)
 * [README.md](./README.md)
 * [.gitignore]()
 * [requirements.txt](./requirements.txt)
 * [setup.py](./setup.py)

