# Vulnerability Search Tool [ oogway ]
## Overview
The Vulnerability Search ( oogway ) Tool is a command-line utility designed to facilitate the search for vulnerabilities and details about Common Vulnerabilities and Exposures (CVEs) using two different sources: VulnersX and SHIFU. This tool provides a simple and efficient way for users to perform various vulnerability-related tasks, including searching for vulnerabilities in specific packages, retrieving detailed information about CVEs, and comparing vulnerabilities between different packages.

SHIFU : https://Github.com/Symbolexe/SHIFU

VulnersX : https://Github.com/Symbolexe/VulnersX

## Features
1. Search for Vulnerabilities using VulnersX

- Description: Allows users to search for vulnerabilities in specific software packages after a specified date.

- Usage: Users can input the package name and the date (in YYYY-MM-DD format) to search for vulnerabilities.

- Output: Displays a list of vulnerabilities found, including their CVE IDs and summaries.

2. Search for Details of a CVE using ShifuCVEFinder

- Description: Enables users to retrieve detailed information about a specific CVE by entering its ID.

- Usage: Users input the CVE ID to search for details.

- Output: Displays information such as the CVE ID, summary, and any associated details.

3. Compare Vulnerabilities between Two Packages

- Description: Allows users to compare vulnerabilities found in two different software packages after a specified date.

- Usage: Users input the names of two packages and the date (in YYYY-MM-DD format) to compare vulnerabilities.

- Output: Displays a list of common vulnerabilities found between the two packages, if any.

4. Simple User Interface

- Description: Provides a clear and concise command-line menu for users to select their desired action.

- Interactive Input: Prompts users for input to specify package names, CVE IDs, and search dates.

- Error Handling: Provides error messages and prompts users to re-enter input in case of invalid choices or errors during the search process.

5. Modular Design

- Description: Utilizes separate modules for interacting with VulnersX and ShifuCVEFinder, promoting code organization and maintainability.

- Flexibility: Enables easy integration of additional vulnerability search sources in the future.

- Pythonic Code: Written in Python, following best practices and conventions for clarity and readability.

6. Interactive and Responsive

- Description: Continuously prompts users for input until they choose to exit, allowing for multiple search queries in a single session.

- Real-time Feedback: Provides real-time feedback during searches to keep users informed of the search progress.

## Installation

To install the Vulnerability Search Tool, simply clone this GitHub repository to your local machine:

```git clone https://github.com/your-username/vulnerability-search-tool.git```

Then, navigate to the project directory and install the necessary dependencies:

```
cd vulnerability-search-tool
pip3 install -r requirements.txt
```
## Usage
After installation, you can run the tool by executing the following command:

```python3 VST.py```

Follow the on-screen instructions to perform various vulnerability-related tasks using the tool.
## Contributions
Contributions to the Vulnerability Search Tool are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
