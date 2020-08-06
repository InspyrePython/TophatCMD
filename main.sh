
version='Alpha 1.0'
counter=0
echo Booting Tophat $version:
echo Type 'y' to accept, 'n' to cancel
read varname
if [ $varname = 'y' ]; then
	clear
	while [ $counter -lt 32 ]; do
    let counter+=1
    echo Loading Assets... $counter/32
		sleep 0.09
		clear
	done
	clear
	python main.py
	
else 
	echo Shutting down Tophat $version
	sleep 9999999
fi