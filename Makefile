# Makefile for redterm

all: redterm regenerate.py display.py config.json

install: all
	mkdir -p ~/.local/bin/redterminal ; true
	cp redterm ~/.local/bin/
	cp {regenerate.py,display.py} ~/.local/bin/redterminal/
	mkdir -p ~/.config/redterminal/ ; true
	cp config.json ~/.config/redterminal/

uninstall: all
	rm ~/.local/bin/redterminal -rf
	rm ~/.local/bin/redterm
	rm ~/.config/redterminal/ -rf
