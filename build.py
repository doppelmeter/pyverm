import subprocess
subprocess.run("python setup.py bdist_wheel", check=True, stdout=True)
user = str(input("username"))
password = str(input("password"))
string = "twine upload -u "+user+" -p "+password+" dist/*"
print(string)
try:
    subprocess.run(string, stdout=True)
except:
    pass
a = input()
