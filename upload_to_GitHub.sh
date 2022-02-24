#!/bin/sh

echo What is your message line?
read msg

cd ~/mycode
git add *
git commit -m "$msg"

