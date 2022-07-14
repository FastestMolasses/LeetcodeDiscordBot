# Leetcode Discord Bot
Sends daily problem to a Discord channel. Tested on Python 3.10.

![python](https://github.com/FastestMolasses/LeetcodeDiscordBot/actions/workflows/main.yaml/badge.svg)

## Installation

1. Setup a Python environment

    ```bash
    $ python -m venv env
    ```

2. In VSCode, make sure you set this environment as the default Python interpreter. This can also be done by pressing `cmd/ctrl + shift + P` and typing ">Python: Select Interpreter", then selecting the newly created environment `./env/bin/python`

3. Enter the environment if you haven't already

    ```bash
    # macOS
    $ source env/bin/activate
    # windows
    $ .\env\Scripts\activate
    ```

4. Install requirements

    ```bash
    $ pip install -r requirements.txt
    ```

5. Rename `.env.sample` to `.env` and fill out the required credentials

6. Run main.py

## Building Docker

Run this command to build the Docker container
```bash
make build-container-dev
```

Then use this command to run the container
```bash
make run-container-dev
```

For building the container for AWS, use
```bash
make build-container
```

## Setting up Terraform and AWS

1. Create a unique bucket name by going to `vars.tf` and updating the default value for the `tf-bucket-name` variable.

2. Update to your bucket name in `tfstate.tf` under the `terraform` block at the bottom of the file.

3. Comment out the `terraform` block all the way at the bottom of the `tfstate.tf` file. This is because Terraform expects the S3 bucket to be already created prior to initializing it.

2. Initialize terraform
    ```bash
    cd terraform/
    terraform init
    ```

3. Apply the terraform code
    ```bash
    terraform apply
    ```

4. Uncomment the `terraform` block that you commented in step 3.

5. Run apply again to create the S3 bucket to hold the terraform state
    ```bash
    terraform apply
    ```
