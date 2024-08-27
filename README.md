# create-tags-securityhub
This Python script automates the process of tagging the AWS Security Hub resource across multiple AWS accounts. It works with a list of AWS profiles specified in the script.

## Prerequisites
- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **AWS CLI**: The AWS CLI should be installed and configured with multiple profiles in the `~/.aws/credentials` file.

## Usage
1. **Ensure Your AWS Profiles are Configured**:
  - The script will process the profiles you specify in the script.
2. **Update the Script**:
  - Modify the `profiles` list in the script to include all AWS profiles you wish to use.
  - Ensure the `region` and `tags` variables in the script are set to the appropriate values for your use case.

## The script will:
  - Retrieve the AWS Security Hub ARN for each profile.
  - Display the current tags, add new ones if needed, and show the updated tags.
