clean:
	python3 setup.py clean --all && rm -rf dist

package:
	#python setup.py sdist
	python3 setup.py sdist bdist_wheel

uninstall:
	python3 -m pip uninstall datastructures_mikeggg

installm:
	tar -xzvf dist/*.tar.gz && cd  dist/

installp:
	python3 -m pip install datastructures_mikeggg-0.1-py3-none-any.whl

printpath:
	python3 -c 'import sys; print(sys.path)'

listmods:
	python3 -m pip list
