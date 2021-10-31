


def convert2arff(num_of_files):
    for ward in range(1, num_of_files + 1):
        fout = open("temp" + str(ward) + ".txt", "w")
        fout.write("@relation patients_temperatures\n")
        fout.write("@attribute patients_ID numeric\n")
        fout.write("@attribute time numeric\n")
        fout.write("@attribute temperatue {High,Low}\n\n")
        fout.write("@data\n")
        fin = open(str(ward) + ".txt", "r")
        for time in range(60 * 12 - 1):
            s = fin.readline().split()
            for patient in range(len(s)):
                if not degreeInRange(s[patient]):
                    s[patient] = far2cel(s[patient])
                if degreeInRange(s[patient]):
                    fout.write(str(patient + 1) + ",")
                    fout.write(str(time) + "," + highOrLow(s[patient]) + "\n")
                else:
                    fout.write(str(patient + 1) + "," + str(time) + ", ?" + "\n")
        fin.close()
        fout.close()


def highOrLow(num):
    if float(num) <= 37:
        return "Low"
    return "High"


def degreeInRange(num):
    if 36 <= float(num) and float(num) <= 43:
        return True
    return False


def far2cel(num):
    num = (float(num) - 32) / 1.8
    return str(round(num, 2))


convert2arff(3)


        
    
