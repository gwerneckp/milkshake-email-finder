# Milkshake Email Finder
Provide the script with a list of names and domains, and it will return a list of emails with hopefully the email of the person you are looking for.

In this example, we will be looking for the email of **Sheldon Cooper** who works at **Caltech university**. We will be calling the script with the following arguments:
names = 'Sheldon Cooper'
domains = 'caltech.</span>edu'

We know beforehand that Sheldon's email is **scooper@caltech.</span>edu**.

After running the program, we obtain the following output:
[
  'sheldon@caltech.edu',
  'sheldoncooper@caltech.edu',
  'coopersheldon@caltech.edu',
  'scooper@caltech.edu',
  'coopers@caltech.edu',
  'sheldonc@caltech.edu',
  'csheldon@caltech.edu',
  'sheldoncooper@caltech.edu',
  'coopersheldon@caltech.edu',
  **'scooper@caltech.edu'**,
  'coopers@caltech.edu',
  'sheldonc@caltech.edu',
  'csheldon@caltech.edu',
  'sheldoncooper@caltech.edu',
  'coopersheldon@caltech.edu',
  'scooper@caltech.edu',
  'coopers@caltech.edu',
  'sheldonc@caltech.edu',
  'csheldon@caltech.edu',
  'cooper@caltech.edu'
]

As you can see, we successfully found Sheldon's email address.

The original PHP code written by my father, Ricardo Paiva, in 2005 is available in this repository. This is a reimplementation of the same algorithm in typescript.
