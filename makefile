start: #start on linux mint
	python3 -m venv .venv
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	sleep 3
	.venv/bin/python3 ./main.py


lint: #format
	.venv/bin/pip freeze > requirements.txt
	# .venv/bin/black .
	# .venv/bin/isort .
	# .venv/bin/autopep8 ./ --recursive --in-place -a
	# .venv/bin/autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./
