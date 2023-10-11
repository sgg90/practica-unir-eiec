.PHONY: all $(MAKECMDGOALS)

# Definir la variable FILENAME con el valor predeterminado "palabras.txt" y la variable IDIOMA a sp
FILENAME ?= palabras.txt
IDIOMA ?= sp

run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py $(FILENAME) yes $(IDIOMA)