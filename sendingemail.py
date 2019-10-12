#!/bin/bash/

SMTPFROM=robtve@gmail.com
SMTPTO=robtve@gmail.com
SMTPSERVER=smtp.googlemail.com:587
SMTPUSER=robtve
SMTPPASS=Nmatar007
messagebody="testing 1 2 3"
subject="anothertest" 

sendEmail -f $SMTPFROM -t $SMTPTO -u $subject -m $messagebody -xu $SMTPUSER -xp $SMTPPASS -s $SMTPSERVER  
