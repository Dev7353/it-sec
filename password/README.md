# Manual

Project for it-security. Calculation of hashes and brute force method.

## Create hashes of passwords within a file

> _python password.py -e inputfile_

the output file contains the hashes

## Calculate a possible combinations (Cartesian product)

> _python password.py -c -l level -s size_

level 1: a-z <br>
level 2: level 1 + A-Z <br>
level 3: level 2 + 0-9 <br>

Number of combinations level^size

## Brute force method to find passwords
This method uses the passwords from point above and hash every entry and
compare this hash with the reference from point one.

> _python password.py -b -x filea -y fileb_

## Additional Notes
Be aware that if you compute combinations for long passwords with level 3,
then you need to calculate about 62^pswLength combnations. For Example,
a length of 6 would mean 62^6  ca. 57 Billion combinations. For a length
of 7 about 3.5 Trillion. Even if you use multithreading or distributed
machines it would take a long time. Better download a rainbow table.

http://project-rainbowcrack.com/table.htm

Be sure you have enough space on your data disk.

