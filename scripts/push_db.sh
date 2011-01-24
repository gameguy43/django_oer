#! /bin/sh
# doesn't quite work yet--need to secretly but automatically pass the password. maybe through .my.cnf

MYSQL_PASS=`cat mysql_pass`
echo $MYSQL_PASS
mysqldump -u ocw_dartmouth -p ocw_dartmouth > thedump.mysql && gzip thedump.mysql && scp thedump.mysql.gz parkcity:/tmp && ssh -t parkcity "zcat /tmp/thedump.mysql.gz | mysql -uocw_dartmouth -p ocw_dartmouth"
#mysqldump -u ocw_dartmouth -p ocw_dartmouth > thedump.mysql && gzip thedump.mysql && scp thedump.mysql.gz parkcity:/tmp && ssh -t parkcity "zcat /tmp/thedump.mysql.gz | mysql -uocw_dartmouth -p ocw_dartmouth"
mv thedump.mysql.gz /tmp/

