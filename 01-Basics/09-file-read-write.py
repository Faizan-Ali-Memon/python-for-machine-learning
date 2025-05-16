with open("funny.text", "r") as f, open("funny_wc.text", "w") as f_out:
    for line in f:
        words = line.split()
        f_out.write(line.strip() + " WordCount: " + str(len(words)) + "\n")
