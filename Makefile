# Makefile for redterm

all: redterm regenerate.py display.py config.json

install: all
	mkdir -p ~/.local/bin/redterminal ; true
	cp redterm ~/.local/bin/
	cp regenerate.py ~/.local/bin/redterminal/
	cp display.py ~/.local/bin/redterminal/
	touch ~/.local/bin/redterminal/__init__.py
	mkdir -p ~/.config/redterminal/data ; true
	cp config.json ~/.config/redterminal/

uninstall: all
	rm ~/.local/bin/redterminal -rf
	rm ~/.local/bin/redterm
	rm ~/.config/redterminal/ -rf
