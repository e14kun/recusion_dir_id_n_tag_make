# id and tag and category make code
## how to run python code
$ python3 main.py

## tree path txt make bash
find target_folder/ -mindepth 1 -type d | xargs -I[] bash -c "echo [] | sed -e 's/\ /\\\\\\\\\ /g' | xargs -I__ bash -c 'echo __ > __/pwd.txt'"
