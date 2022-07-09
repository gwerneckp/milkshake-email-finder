# Milkshake Email Finder
Provide the script with a list of names and domains, and it will return a list of emails with hopefully the email of the person you are looking for.

In this example, we will be looking for the email of **Sheldon Cooper** who works at **Caltech university**. We will be calling the script with the following arguments:</br>

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

The original PHP code written by my father, Ricardo Paiva, in 2005 is available in this repository. This is a reimplementation of the same algorithm in typescript.
