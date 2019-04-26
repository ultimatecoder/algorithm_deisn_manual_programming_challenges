lint:
	flake8
test:
	cd problems && python -m unittest
end-to-end-test:
	garud end_to_end_tests
