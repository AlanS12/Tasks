
name=input("\n\tEnter a file name: ")

data={"py":"Python Source Code File","cpp":"C++ Source Code File","c":"C Source Code File","java":"Java Source Code File","cs":"C# Source Code File","html":"HTML File","js":"JavaScript Source Code File","pl":"Perl Source Code File","xml":"XML File","doc":"MS Word File","xls":"MS Excel File","ppt":"MS PowerPoint File","txt":"Plain Text File","csv":"Comma Separated Values File","bmp":"Bitmap File","gif":"Graphical Interchange Format","xlsx":"MS Excel Open XML File","db":"Database File","sql":"SQL File","exe":"Windows Executable File","sys":"Windows System File","tmp":"Temporary","torrent":"BitTorrent File"}

split_info=name.split('.')

if split_info[1] in data:
    print("\tThe extension of the file '" + name + "' : " + data[split_info[1]])
elif split_info[1] not in data:
    print("\t--Sorry, we could not recognise this file extension.--")
