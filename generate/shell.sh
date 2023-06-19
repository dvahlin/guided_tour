#!/bin/bash

# Function to generate Lorem Ipsum text
generateLoremIpsum() {
  local size=$1
  local loremIpsum="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed consequat eleifend mi id dignissim. Maecenas et justo id lorem sagittis condimentum vitae a eros. Nullam rhoncus, felis ac feugiat consequat, enim mauris semper dui, id vulputate ipsum nisi non massa. Aliquam erat volutpat. Nulla facilisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi pellentesque imperdiet libero vitae commodo. Sed interdum metus eu leo rhoncus consequat. Sed non consectetur felis, vitae luctus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed nec ipsum vel mi auctor condimentum vel a elit. Fusce non orci fringilla, eleifend tellus id, sollicitudin sem. Nulla facilisi."

  # Repeat the Lorem Ipsum text to match the desired size
  local loremIpsumText=$(printf "%0.s$loremIpsum " $(seq 1 $((size / ${#loremIpsum} + 1))))

  # Trim the text to the desired size
  echo ${loremIpsumText:0:$size}
}

# Generate 100 files with different sizes
for ((i=1; i<=100; i++))
do
  if [[ $i -eq 42 ]]; then
    filename="UxIXGZPa6l.txt"
    filesize=242
  else
    filename=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1).txt
    filesize=$((RANDOM % 301 + 200))
  fi

  loremIpsumText=$(generateLoremIpsum $filesize)

  # Create the file with Lorem Ipsum text
  echo "$loremIpsumText" > $filename
  echo "Generated $filename with size $filesize bytes."
done

