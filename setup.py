from setuptools import setup, find_packages
from sample.info import __package_name__, __version__

with open('README.md', 'r', encoding='utf-8') as f:
	readme = f.read()
with open('requirements.txt', 'r', encoding='utf-8') as f:
	requires = f.read().splitlines()

setup(
	name=__package_name__,                                       # 해당 파이썬 패키지의 이름 (info.py 참고)
	version=__version__,                                         # 배포 버전 (info.py 참고)
	long_description=readme,                                     # 패키지에 대한 설명
	packages=find_packages(exclude=["contrib","docs","tests"]),  # 프로젝트에 포함되는 패키지 리스트 (__init__.py 찾음)
	package_data={'': ['*.yaml','*.yml']},                       #
	install_requires=requires,                                   # 필요 패키지 목록 (requirements.txt 활용)
	setup_requires=[                                             # 빌드에 필요한 패키지 목록, python setup.py 실행전
		"pytest-runner",
	],
	#test_require=test_requires,
	python_requires=">3.6",                                      # 필요 버전
	entry_points={                                               # 패키지 설치 후, shell에서 실행 가능한 명령어 지정, srtest-python을 명령창에서 실행하면, srtest 폴더의 main.py 내에 정의 된 main 함수가 실행 됨
		"console_scripts": ["srtest-python=srtest.main:main"]
	},
	classifiers=[                                                # PyPi 에 등록될 메타 데이터 설정(환경, 버전, GUI 여부 등)
		'Environment :: Console',
		'Operating System :: POSIX :: LINIX',
		'Programming Language :: Python :: 3.6'
	]
)
