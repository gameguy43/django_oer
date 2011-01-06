#! /bin/sh

scp mysite/site_database.sqlite3 parkcity:/tmp/
ssh parkcity 'ls ~/webs/ocw-dartmouth-site/mysite/; mv /tmp/site_database.sqlite3 ~/webs/ocw-dartmouth-site/mysite/'

