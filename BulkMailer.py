import argparse
import smtplib
from milkshake import MailGenerator
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("--email", "-e", help="Your email address")
parser.add_argument("--password", "-p", help="Your email password")
parser.add_argument("--subject", "-s", help="Subject of the email")
parser.add_argument("--message", "-m", help="Body of the email")
parser.add_argument("--name", "-n", help="Full name of recipient")
parser.add_argument("--domains", "-d", help="Possible domains for email address")
parser.add_argument("--wizard", "-w", help="Prompt user for missing arguments", action="store_true")
parser.add_argument("--delay", "-l", help="Delay in seconds between each email", type=int, default=5)
parser.add_argument("--smtp", "-t", help="SMTP server", default="smtp.gmail.com")
parser.add_argument("--port", "-o", help="SMTP port", type=int, default=587)
parser.add_argument("--verbose", "-v", help="Verbose mode", action="store_true")

args = parser.parse_args()


def verbose(msg):
    if args.verbose:
        print(msg)


fields = [("email", "Type your email: "),
          ("password", "Type your email password: "),
          ("subject", "Type the subject of the email: "),
          ("message", "Type the body of the email: "),
          ("name", "Type the full name of the recipient: "),
          ("domains", "Type the possible domains for the recipient's email address: ")]

for field, prompt in fields:
    if not getattr(args, field):
        if args.wizard:
            setattr(args, field, input(prompt))
        else:
            parser.error(f"--{field} or -{field[0]} is required")

# Connect to the Gmail server
verbose(f"Connecting to {args.smtp}:{args.port}")
server = smtplib.SMTP(args.smtp, args.port)

# Start TLS encryption
verbose("Starting TLS encryption")
server.starttls()

# Login to the Gmail account
verbose("Logging in")
server.login(args.email, args.password)

# List of email addresses to send the email to
verbose("Generating email addresses")
recipients = MailGenerator().generate(args.name, args.domains)

# Email message to send
verbose("Constructing email message")
subject = args.subject
message = args.message
final_message = f"""Subject: {subject}

{message}"""

# Confirm the final email
confirm = input(f"\nConfirm that you want to send this email:\n{final_message}\n(Y/n)")
if confirm not in ["y", '']:
    print("Email not sent")
    exit()
verbose("User confirmed email")
# Confirm the recipient list
recipients_list = '\n'.join(['-' + item for item in recipients])
confirm = input(
    f"\nConfirm that you want to send this email to the following {len(recipients)} recipients:\n{recipients_list}\n(Y/n)")
if confirm not in ["y", '']:
    print("Email not sent")
    exit()
verbose("User confirmed recipients")
# Send the email to each recipient
print()
print("Sending emails...")
for recipient in recipients:
    server.sendmail('gwerneckpaiva@gmail.com', recipient, message)
    # Add a delay to avoid tripping spam filters
    print(f'Email sent to {recipient}')
    sleep(5)

# Disconnect from the server
server.quit()
