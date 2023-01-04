# Milkshake Email Finder

Provide the script with a list of names and domains, and it will return a list of emails with hopefully the email of the
person you are looking for.

In this example, we will be looking for the email of **Sheldon Cooper** who works at **Caltech university**. We will be
calling the script with the following arguments:</br>

**names = 'Sheldon Cooper'**</br>
**domains = 'caltech.</span>edu'**</br>

We know beforehand that Sheldon's email is **scooper@caltech.</span>edu**.

After running the program, we obtain the following output:</br>

[</br>
'sheldon@caltech.edu',</br>
'sheldoncooper@caltech.edu',</br>
'coopersheldon@caltech.edu',</br>
**'scooper@caltech.edu'**,</br>
'coopers@caltech.edu',</br>
'sheldonc@caltech.edu',</br>
'csheldon@caltech.edu',</br>
'sheldon.cooper@caltech.edu',</br>
'cooper.sheldon@caltech.edu',</br>
's.cooper@caltech.edu',</br>
'cooper.s@caltech.edu',</br>
'sheldon.c@caltech.edu',</br>
'c.sheldon@caltech.edu',</br>
'sheldon_cooper@caltech.edu',</br>
'cooper_sheldon@caltech.edu',</br>
's_cooper@caltech.edu',</br>
'cooper_s@caltech.edu',</br>
'sheldon_c@caltech.edu',</br>
'c_sheldon@caltech.edu',</br>
'cooper@caltech.edu'</br>
]</br>

As you can see, we successfully found Sheldon's email address.</br>

This repository contains the original PHP code written by my father, Ricardo Paiva, in 2005, as well as the typescript
reimplementation. The Python script is a new and improved solution that will generate more email options than the
previous one.

# BulkMailer

BulkMailer is a command-line script that allows you to send emails to a list of recipients in bulk. It takes in a
variety of arguments to customize the email and the recipients.

### Required arguments:

* **--email/-e:** Your email address. This is the address that the emails will be sent from.

* **--password/-p:** Your email password. This is needed to log in to your email account and send the emails.

* **--subject/-s:** The subject of the email.

* **--message/-m:** The body of the email.

* **--name/-n:** The full name of the recipient. This will be used to generate a list of potential email addresses for
  the recipient.

* **--domains/-d:** A list of possible domains for the recipient's email address. For example, if the recipient works at
  Caltech university, you might include 'caltech.edu' in this list.

### Optional arguments:

* --wizard/-w: If this flag is provided, the script will prompt the user for any missing arguments (i.e. those that are
  required but not provided on the command line).

* **--delay/-l:** The delay in seconds between each email. This can be used to avoid tripping spam filters. The default
  value is 5 seconds.

* **--smtp/-t:** The SMTP server to use for sending the emails. The default value is 'smtp.gmail.com'.

* **--port/-o:** The port to use when connecting to the SMTP server. The default value is 587.

* **--verbose/-v:** If this flag is provided, the script will print out debugging information as it runs.

Here is an example of how you might use the script:</br>
`python BulkMailer.py -e myemail@example.com -p mypassword -s 'Hello World' -m 'This is a test email' -n 'Sheldon Cooper' -d 'caltech.edu gmail.com'`

This will send an email with the subject 'Hello World' and the message 'This is a test email' to all of the potential
email addresses for Sheldon Cooper at 'caltech.edu' and 'gmail.com'.



