ENC_FILE := archivo.pdf.gpg
LST_FILE := dict.py
MAIN := main.py
PYT3 := python3
WRD_LST := wordlist.txt

CODE_IN := --file $(ENC_FILE) --wordlist $(WRD_LST)

all:
	$(PYT3) $(LST_FILE)
	$(PYT3) $(MAIN) $(CODE_IN)
