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


## Keyword arguments like http://amoffat.github.io/sh/#keyword-arguments

# resolves to "curl http://duckduckgo.com/ -o page.html --silent"
curl("http://duckduckgo.com/", o="page.html", silent=True)

# or if you prefer not to use keyword arguments, this does the same thing:
curl("http://duckduckgo.com/", "-o", "page.html", "--silent")

# resolves to "adduser amoffat --system --shell=/bin/bash --no-create-home"
adduser("amoffat", system=True, shell="/bin/bash", no_create_home=True)

# or
adduser("amoffat", "--system", "--shell", "/bin/bash", "--no-create-home")
```
