import winreg

HKCU = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)


def fetch_reg(key):
    """Return given key's value from steam registry path."""

    if key in ('pid', 'ActiveUser'):
        reg_path = r"Software\Valve\Steam\ActiveProcess"
    else:
        reg_path = r"Software\Valve\Steam"

    value = None
    try:
        reg_key = winreg.OpenKey(HKCU, reg_path)
        value_buffer = winreg.QueryValueEx(reg_key, key)
        value = value_buffer[0]
        winreg.CloseKey(reg_key)
    except OSError as err:
        print(err)
    return value


def registry_magic(name: str) -> None:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "AutoLoginUser", 0, winreg.REG_SZ, name)
    winreg.SetValueEx(key, "RememberPassword", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)
