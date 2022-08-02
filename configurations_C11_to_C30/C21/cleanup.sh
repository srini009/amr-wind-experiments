#!/bin/bash
rm -rf plt* chk* *.png addr.* nodes.* 
rm *.log *.error *.output *.cobaltlog
rm -rf core* sdskv.add *.txt rp.session* *.mercury
for i in {1..17}
do 
	rm -rf $i
done
rm STDOUT
