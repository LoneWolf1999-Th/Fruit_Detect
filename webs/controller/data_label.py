def all_label():
    classes = []
    classes_label = []
    with open("webs/text/data_label.txt", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    for x in classes:
        if x not in classes_label:
            classes_label.append(x)

    return(classes_label)

