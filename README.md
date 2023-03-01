# SLAC. Steam Lightweight Account Changer

If you prefer Batch Script version, download it [here](https://github.com/Zipliks/account-changer-batch)

## How does it work
Steam stores it's data in `Steam/config/login.vdf`.
So my idea was to read that file, parse all those cached accounts and switch between them using registry.

There is no GUI yet, but it's planned. Some day.
The rule to get GUI version ETA:
1. Tomorrow
2. If not yet, read point 1

Executable binary was built using [Nuitka](https://pypi.org/project/Nuitka/).

Used build command: 
```
python -m nuitka --standalone --onefile slac.py
```
## How does it look like
White text is account name/login. Yellow text is current profile name or alias.

![image](https://user-images.githubusercontent.com/4831847/222280287-77eff2b2-7d56-40aa-977c-e0139b739e29.png)
