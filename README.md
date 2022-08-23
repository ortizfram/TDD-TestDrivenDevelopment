# TDD-UNIT TESTING
Learn Test Driven Development with Python
**LINKS:**

[Unittest assert methods](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)

## ㊗️ INSTALLATION
- donwload virtualenv [create virtualenv windows 2022](https://gist.github.com/ortizfram/f08ca70b8bf24ddd8eb13fd5b0649476)

## ㊗️RULES of TDD
⚪ not allowed to write a piece of code before a failing test 

⚪ write just enough test to fail 

⚪ write just enough code to pass 

## ㊗️ creation of directories
     mkdir static 
     mkdir templates
     mksdir test

## ㊗️ keep code DRY:
❗to not repeat your code-pieces along the code

❗setUp = `runs code before every single test`

❗tearDown = `runs code after every single test`

     @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')
