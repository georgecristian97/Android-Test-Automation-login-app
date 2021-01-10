# Android-Test-Automation-login-app



Getting started:

:package:	Install Java:

:package:	Install android studio:

:warning:	mac  users, try adb devices if does not work then:

   -	Start Terminal
          					command + spacebar, enter terminal and click terminal app

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

```
brew install android-platform-tools
```

```
 adb devices
```



​	 :computer:Check in terminal if Java is installed: 

​			java -version

​			javac -version

​			:trollface: if error set env var for :warning: ​windows:

​				-in explorer paste:

​					Control Panel\System and Security\System

​				-go to:

​					Advanced system settings - > Environment Variables

​						1) System variables - > New 

​							-set the name: JAVA_HOME 

​							-set the value: C:\Program Files\Java\jdk1.8.0_261

​						2) System variables - > Path - > New

​							-set the value: %JAVA_HOME%\bin

​				 -check again:

​					java -version

​                    javac -version

​                    :smile:	Now is should be fine

:package:	[Download and install Appium](http://appium.io/downloads.html) and set the env var:

![](https://raw.githubusercontent.com/georgecristian97/Android-Force-Close-Apps/main/Screen%20Shot%202021-01-10%20at%207.30.28%20PM.png)	

:package:	[Install python](https://www.python.org/downloads/release/python-370/)

:hammer:	Edit with:

[Download PyCharm: Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/download/#section=windows)

pip install Appium-Python-Client



Without configuring your pycharm you can right click on python file and run a test by having those in the file:

```python
import unittest
class test_1(unittest.TestCase):
  #.........
  def testAnything(self):#any test should start with "test" 
    #test code
    
if __name__ == '__main__':
   unittest.main()
```

