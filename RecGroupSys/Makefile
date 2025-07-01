# Makefile para el proyecto RecGroupSys

# Usar BASH para una sintaxis más robusta y evitar problemas de shell.
SHELL := /bin/bash

# Define el intérprete de Python a usar.
# Esto permite flexibilidad si se usan diferentes entornos virtuales (p. ej. .venv/bin/python).
PYTHON := python

# Evita que make se confunda con archivos que tengan el mismo nombre que los targets.
# .PHONY declara que estos no son archivos.
.PHONY: help test build clean

# El target 'default' se ejecuta si solo escribes 'make' en la terminal.
default: test

## test: Ejecuta las pruebas unitarias con pytest sin instalar la librería.
test:
	@echo "---TEST---"
	@$(PYTHON) -m pytest

## build: Construye la libreria y la instala en el entorno actual.
build:
	@echo "---BUILD---"
	@$(PYTHON) -m build
	@$(PYTHON) -m pip install .
	@echo "Done BUILD"

## clean: Elimina los artefactos de construcción y la caché de Python.
clean:
	@echo "---CLEAN---"
	@rm -rf build dist *.egg-info .pytest_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Done CLEAN"

install: build clean