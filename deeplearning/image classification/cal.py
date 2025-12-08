time = 0

with open("epoch.txt", "r") as f:
    for line in f:
        epochs = line.strip()
        seconds = epochs[25:27]
        if seconds.isdigit():
            time += int(seconds)

print("Total time taken for training the model is {} minute".format(time / 60))