indian = ["samosa", "daal", "naan"]
pakistani = ["chicken", "mutton", "rice"]
chinese = ["pasta", "pizza", "fries"]

dish = input("Enter the dish: ").lower()

if dish in indian:
    print("The dish is Indian")
elif dish in pakistani:
    print("The dish is Pakistani")
elif dish in chinese:
    print("The dish is Chinese")
else:
    print("The dish is not found in the list")
