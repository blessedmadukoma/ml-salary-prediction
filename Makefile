lint:
	isort app.py
	flake8 app.py

run:
	streamlit run app.py

.PHONY: lint run