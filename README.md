## process

Inspired by sh.

### Usage

```
from process import process

git = process.git
git.status()

ls = process.bake('ls')
ls('-al')
ls('-l', '-a')
ls('-l', a=True)
ls.call('-al')
process.ls.call('-al')
```
