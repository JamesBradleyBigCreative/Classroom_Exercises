from file_read_backwards import FileReadBackwards

def _12_Days_Of_Christmas():
    with FileReadBackwards("MyFile.txt", encoding="utf-8") as frb:

        Input = int(input("\nWhat day of christmas is it: "))
        final = []

        while Input > 0:
            x = frb.readline()

            final.append(x)
            Input -= 1

            if Input == 0:

                Choice = input("\nDo you want to try again| 'Y' or 'N': ")

                Choice = Choice.upper()

                if Choice == 'Y':
                    i  = (len(final)) -1
                    while i >= 0:
                        print(final[i])
                        i -= 1

                    Input = int(input("\nWhat day of christmas is it: "))

                elif Choice == 'N':

                    i  = (len(final)) -1
                    while i >= 0:
                        print(final[i])
                        i -= 1

