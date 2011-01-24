#! /bin/bash
ssh -t parkcity "cd webs/ocw-dartmouth-site/ && git pull && sudo /etc/init.d/apache2 reload"
