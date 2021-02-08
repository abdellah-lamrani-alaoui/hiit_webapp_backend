#!/bin/bash

for filename in  static/images/raw_images/*;
do
 echo " converting $filename"
 convert $filename -resize 300x500 "static/images/retreated_images_300_500/$(basename "$filename")"
done
