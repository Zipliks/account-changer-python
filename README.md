# SLAC. Steam Lightweight Account Changer

If you prefer Batch Script version, download it [here](https://github.com/Zipliks/account-changer-batch)

## How does it work
Steam stores it's data in `Steam/config/loginusers.vdf`.<br>
So my idea was to read that file, parse all those cached accounts and switch between them using registry.<br>
To make it work correctly, each account you want to switch to must be logged in at least once. Do not forget to check `Remember me`.<br>
By that, all your logged in accounts will be stored in `loginusers.vdf` I mentioned previously.

![image](https://user-images.githubusercontent.com/4831847/222281473-e3162a3c-4a8b-4200-b802-b1988a043699.png)



## How does it look like
White text is account name/login. Yellow text is current profile name or alias.

![image](https://user-images.githubusercontent.com/4831847/222280287-77eff2b2-7d56-40aa-977c-e0139b739e29.png)

## About SLAC
There is no GUI yet, but it's planned. Some day.
The rule to know GUI version ETA:
1. Tomorrow
2. If not yet, read point 1

Executable binary was built using [Nuitka](https://pypi.org/project/Nuitka/).<br>
Used build command: 
```
python -m nuitka --standalone --onefile slac.py
```
