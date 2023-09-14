from bs4 import BeautifulSoup
import os
from robot.rebot import rebot
import sys


def main(output_file_basename: str = None):
    content = []
    # BROKEN_OUTPUT_FILE is an environment variable that
    # is a name of the broken output file without .xml extension
    # by default it is "output" meaning "output.xml"

    broken_output_file = output_file_basename or os.getenv("BROKEN_OUTPUT_FILE", "output")
    fixed_output_xml = f"{broken_output_file}_fixed.xml"
    fixed_output_html = f"{broken_output_file}_fixed.html"

    with open(f"{broken_output_file}.xml", "r") as file:
        content = file.readlines()
    soup = BeautifulSoup("".join(content), 'lxml-xml')
    with open(fixed_output_xml, "w") as file:
        file.write(soup.prettify())
    rebot(fixed_output_xml, log=fixed_output_html, report=None)

    last_keyword_before_not_run = None
    keywords = soup.find_all('kw')

    # Traverse through the keywords to find the last one before a "NOT RUN" status
    for kw in keywords:
        status = kw.find('status')  # Find the status element within the keyword element
        if status:
            status_value = status.get('status', 'UNKNOWN')  # Get the status attribute, default to 'UNKNOWN' if not present
            if status_value == 'NOT RUN':
                break  # Stop searching when a "NOT RUN" status is encountered
            last_keyword_before_not_run = kw  # Update the last keyword before a "NOT RUN" status

    # Output the last keyword before a "NOT RUN" status (if found)
    if last_keyword_before_not_run is not None:
        print("\nLast keyword before 'NOT RUN':")
        print(last_keyword_before_not_run.prettify())
    else:
        print("\nNo keyword found before a 'NOT RUN' status.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) == 2 else None)
