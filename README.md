	conda create -n my_kivy_project
	source activate my_kivy_project
	conda install -n my_kivy_project -c conda-forge kivy cython

## command line after INSTALLING SUBLIME TEXT 
	/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl .

- in `.bash_profile`

	export PATH=/bin:/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin:$PATH

	sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl

## install Brew 
	brew install autoconf automake libtool pkg-config
	brew link libtool
	sudo easy_install pip
	conda install -n my_kivy_project -c conda-forge cython

## to complie
	git clone git://github.com/kivy/kivy-ios

	> read requirements
	git clone https://github.com/kronenthaler/mod-pbxproj.git
	sudo python setup.py install

	conda install -n my_kivy_project -c conda-forge Pillow requests cookiecutter

	sudo pip3 install kivy-ios

Make sure that I have a right version of Xcode.
- The detail in kivy-iso README

	toolchain build python3 kivy

Some more things I needed
	conda install -n my_kivy_project -c conda-forge sh
	sudo pip install pbxproj

## Create an Xcode project

The main application's entry point must be named main.py before creating the Xcode project.
	toolchain create test-cal /Users/hyunju/learn-kivy/learn-kivy/intro/06_Kivy_app

