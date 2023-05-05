#!/bin/bash

# Script to run code_analyzer on all files in the test_files directory

test_files_dir="./test_files"
output_dir="./test_files"

# Create the output_files directory if it doesn't exist
mkdir -p "$output_dir"

# Iterate through all files in the test_files directory
for test_file in "$test_files_dir"/*; do
  # Get the file extension and name without extension
  file_extension="${test_file##*.}"
  file_name="$(basename "$test_file" ".$file_extension")"

  # Set the output file path
  output_file_path="$output_dir/${file_name}.ai-version.${file_extension}"

  # Run the code_analyzer on the test file and save the result to the output file
  echo "Analyzing file: $test_file"
  code-analyzer "$test_file" "$output_file_path"
  echo "Improved code saved to: $output_file_path"
  echo
done
