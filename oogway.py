# Creator : Yasin Saffari ( Symbolexe )
# Date : 2024-04-19

#SHIFU : https://github.com/Symbolexe/SHIFU
#VulnersX : https://github.com/Symbolexe/VulnersX

from shifucvefinder import search_by_cve_id
from vulnersx import VulnersX

def main():
    print("Welcome to oogway - Vulnerability Search Tool!")

    # Initialize instances of VulnersX and ShifuCVEFinder
    vulnersx = VulnersX()

    while True:
        print("\nChoose an option:")
        print("1. Search for vulnerabilities using VulnersX")
        print("2. Search for details of one or more CVEs using ShifuCVEFinder")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Search for vulnerabilities using VulnersX
            package_name = input("Enter the package name to search for vulnerabilities: ")
            after_date = input("Enter the date (YYYY-MM-DD) to search for vulnerabilities after: ")

            vulnerabilities = vulnersx.search_vulnerabilities(package_name, after_date)
            if vulnerabilities:
                print(f"Found {len(vulnerabilities)} vulnerabilities after {after_date} for {package_name}")
                for vulnerability in vulnerabilities:
                    print(vulnerability)
            else:
                print(f"No vulnerabilities found after {after_date} for {package_name}")

        elif choice == "2":
            # Search for details of one or more CVEs using ShifuCVEFinder
            print("Do you want to enter CVE IDs manually (M) or from a file (F)?")
            method = input("Enter M or F: ")

            if method.upper() == "M":
                cve_ids = input("Enter one or more CVE IDs separated by commas: ").split(',')
            elif method.upper() == "F":
                file_path = input("Enter the path to the file containing CVE IDs: ")
                with open(file_path, 'r') as file:
                    cve_ids = file.read().splitlines()
            else:
                print("Invalid input. Please try again.")
                continue

            for cve_id in cve_ids:
                print(f"\nCVE Information for {cve_id}:")
                search_by_cve_id(cve_id)

        elif choice == "3":
            print("Exiting the oogway - Vulnerability Search Tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
