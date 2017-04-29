TARGET := "$${HOME}/Library/Application\ Support/Sublime\ Text\ 3/Packages/User"

all: fmtdark deploydark

fmtdark:
	TEMPFILE=$$(mktemp); \
	(jq -M --tab "." < syntax.dark.json) 1> "$$TEMPFILE"; \
	mv -v -- "$$TEMPFILE" syntax.dark.json 2> /dev/null

fmtlight:
	TEMPFILE=$$(mktemp); \
	(jq -M --tab "." < syntax.light.json) 1> "$$TEMPFILE"; \
	mv -v -- "$$TEMPFILE" syntax.light.json 2> /dev/null

deploydark:
	TEMPFILE=$$(mktemp); \
	python generator.py "syntax.dark.json" 1> "$$TEMPFILE"; \
	mv -v -- "$$TEMPFILE" "${TARGET}/Monnokay.tmTheme"

deploylight:
	TEMPFILE=$$(mktemp); \
	python generator.py "syntax.light.json" 1> "$$TEMPFILE"; \
	mv -v -- "$$TEMPFILE" "${TARGET}/Monnokay.tmTheme"
