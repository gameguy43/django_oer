#! /bin/sh
# doesn't quite work yet--need to secretly but automatically pass the password. maybe through .my.cnf

mysqldump -u ocw_dartmouth -p ocw_dartmouth > thedump.mysql && gzip thedump.mysql && scp thedump.mysql.gz parkcity:/tmp && ssh parkcity "zcat /tmp/thedump.mysql.gz | mysql -uocw_dartmouth -p ocw_dartmouth"
mv thedump.mysql.gz /tmp/

