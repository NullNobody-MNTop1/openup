## What is openup?
  A python module that makes full screening easy. Just like F11 for cmd, but automatic and mid execution.

## How To Install:
  1. Open the folder in VS Code(or something similar. Must have a built-in terminal/command prompt. If you do not have built-in terminal/command prompt, skip to "How To Install Through CMD")
  2. Write: pip3 install . (if you do not have pip3 you can use pip)
  3. Use import openup to use it in your projects.

## How To Install Through CMD:
  1. Open CMD(command prompt)
  2. Navigate to the folder containing isit.py and pyproject.toml files using "cd" command
  3. Write: pip3 install . (if you do not have pip3 you can use pip)
  4. Use import openup to use it in your projects

## How To Use:
### Example:
```python
import openup
openup.force_full_screen() #This will force full screen if ran through cmd (does not work with built in terminals in editors like VS code)
```

### Alternative Example:
```python
from openup import force_full_screen as ffs;
ffs() #Same as previous example (it does not let me make it multiline.)
```
