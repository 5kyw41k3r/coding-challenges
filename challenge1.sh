echo "Enter an array to be reversed:" # Asks the user to input an array
read -a array # -a flag for reading input as array

min=0
max=$(( ${#array[@]} -1 )) # first value from reverse

while [[ min -lt max ]]
do
    # Swap current value from respective reverse value
    x="${array[$min]}" # VERY IMPORTANT... So values in the middle don't cause trouble
    array[$min]="${array[$max]}" # turn min to max
    array[$max]="$x" # turn max to min

    # Move closer to the values
    (( min++, max-- ))
done

# Print out the arrays
echo "${array[@]}"
