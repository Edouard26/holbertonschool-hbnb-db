#!/bin/bash

# Start the server in the background
python manage.py runserver 0.0.0.0:5000 &

# Wait for the server to start
sleep 5

# Run the tests
pytest

# Capture the exit code from pytest
EXIT_CODE=$?

# Kill the server
SERVER_PID=$(pgrep -f runserver)
kill -9 $SERVER_PID

# Exit with the pytest exit code
exit $EXIT_CODE
```

Make this script executable:
```sh
chmod +x test_runner.sh
```

### Run the Test Runner Script:

Execute the test runner script to start the server, run tests, and clean up:

```sh
./test_runner.sh
```