# Secret Santa Assigner
This package is for generating secret santa assignees and notifying them via the Twilio SMS API

## Usage
#### `secret_santa.py run`
This command will assign secret santas and notify them of their assignments
#### `secret_santa.py test_run`
This command will assign secret santas and print the assignments out to the console
#### `secret_santa.py test_sms`
This will send a test SMS message to the test number specified in **twilio.yml**

## Configuration
* **santas.yml** is used to configure contact info for santas and to specify constraints on who cannot be assigned to each other
* **twilio.yml** is used to configure the Twilio SMS client
