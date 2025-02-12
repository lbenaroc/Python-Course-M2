ADD_URL=http://localhost:5001/add
SUB_URL=http://localhost:5001/subtract
.PHONY: run test

run:
	python app.py

test:
	python test.py

test-api:
	curl -X POST -H "Content-Type: application/json" -d '{"a": 2, "b":3}' $(ADD_URL)
	curl -X POST -H "Content-Type: application/json" -d '{"a": 2, "b":3}' $(SUB_URL)

test-api-async:
	python3 test-api.py