# BC ferries avg monthly delay calculator
This is an interactive program to decode a data set of encrypted ferry schedules from BC Ferries. The program interactively prompts the user for input which is used to decrypt and process the appropriate files.

Program Flow:
1. Ask user for a encrypted filename;
2. Check if file exists, if not, prompt user again;
3. The password (key) to decode the file;
4. Check if the password is in a valid format, if not, prompt the user again;
5. Check if the provided valid password successfully decrypts the provided file,
if not, prompt the user for the password again;
6. Iterate through the decrypted rows;
7. Calculate the average monthly delay between scheduled time and when the
ferry actually leaves the port;  


User Input:  

This program prompts the user for the encrypted file to decode and the password (key) to use. It validate the data upon input. If the data is invalid, it notifies the user of their error and prompts them to enter their selections again.   

The user is also be able to enter q for quit at either prompt.  


Password Validity:  

A valid password must have:
1. At least 1 uppercase letter;
2. At least 2 numerical digits;
3. Exactly 2 special characters, !@#$&*-_
4. password length of 6-8 characters;  


Output:  

The decrypted file will contain information on BC Ferries on their sailing schedules for some months. This program calculates the average departure delay for each month in the file. These files will have data for some, but not all, months. Months for which there is no data is ignored. For each month in the file, the program outputs the line Average departure delay for MON: AVG, where MON is the 3 letter month abbreviation and AVG is the average delay in minutes rounded to 2 decimal places for each month.
