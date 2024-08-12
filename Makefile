test:
	@echo Run test
	pytest -m only --headless --browser==chrome --reruns 5 -n 5

test_head:
	@echo Run test
	pytest -m only --headless=yes --browser==chrome --reruns 5 -n 5

test_firefox:
	@echo Run test
	pytest -m only --headless=yes --browser==firefox --reruns 5 -n 5

update:
	pip install -r requirements.txt

test:
	pytest --reruns 5