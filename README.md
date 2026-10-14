 Cloud Misconfiguration Detection and Reporting Tool

 1. Project Overview

The Cloud Misconfiguration Detection and Reporting Tool is a cybersecurity project designed to identify potential security misconfigurations in cloud storage environments. It focuses on detecting configuration issues that could expose sensitive data or weaken storage security.

The project uses a simulated cloud storage environment powered by MinIO, which provides an S3-compatible object storage service. The tool aims to identify security weaknesses and present findings with recommendations to help users improve their cloud storage security.

 2. Project Objectives

- Identify potentially insecure cloud storage configurations.
- Detect overly permissive bucket access policies.
- Check relevant storage security settings, including encryption where supported.
- Record detected security issues and supporting evidence.
- Generate security findings and remediation recommendations.
- Evaluate the tool using secure and intentionally misconfigured test environments.

 3. Technologies Used

- Python: Core programming language.
- Flask: Web application framework, if used in the implementation.
- MinIO: Local S3-compatible storage environment for testing.
- Boto3 or another S3-compatible client: For storage interaction, if used.
- Git and GitHub: Version control and project documentation.

 4. How It Works

1. Connect to the configured MinIO storage environment.
2. Retrieve supported bucket configuration and security settings.
3. Evaluate the settings against defined security checks.
4. Record detected misconfigurations and relevant evidence.
5. Organise the scan results.
6. Present the findings and recommendations in a security report, where implemented.

5. Test Environment

The tool is evaluated using simulated cloud storage buckets, including:

- `test-bucket`
- `analytics-data`
- `backup-archive`
- `user-uploads`

The evaluation environment includes secure configurations and intentionally misconfigured configurations. These are used to assess whether the tool can distinguish between expected secure settings and potential security weaknesses.

 6. Project Screenshots

 Application Interface (https://capstone-1-two.vercel.app/)




 7. Running the Project

The exact setup depends on the project's current implementation. If the application uses Flask and Python dependencies, the general setup may look like this:

1. Clone the repository:

   ```bash
   git clone https://github.com/Huffaz-123/cloud-misconfiguration-detector.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cloud-misconfiguration-detector
   ```

3. Create and activate a Python virtual environment.

4. Install the required dependencies listed in `requirements.txt`, if provided.

5. Configure the MinIO endpoint and credentials using environment variables or a local configuration file.

6. Start MinIO and run the application using the appropriate entry point for the project.

Note: Confirm the application's actual entry point and setup instructions before publishing these steps as verified instructions.

 8. Security Considerations

- Use a local test environment or an environment you are authorised to assess.
- Do not commit passwords, access keys, tokens, or other secrets to GitHub.
- Use test data rather than sensitive production data.
- Keep intentionally misconfigured buckets isolated from public or production environments.

 9. Current Development Status

This project is being developed and evaluated as part of a cybersecurity project focused on cloud storage security. Its detection capabilities and reporting features should be assessed against the defined test cases before final performance claims are made.

#10. Author

Ababalwe Mvumbi

BSc Mathematics and Computer Science  
Sol Plaatje University

Project: Cloud Misconfiguration Detection and Reporting Tool
