from apachelogs import LogParser        #Firstly Install pip install apachelogs

status_code_dict = {}

parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")


with open("C://Users//H P//Downloads//access_log") as f:         #File location where the access log file is present
    for line in f:
        entry = parser.parse(line)
        status_code = entry.final_status

        if status_code not in status_code_dict:
            status_code_dict[status_code] = 1
        else:
            status_code_dict[status_code] += 1

for i in status_code_dict:
     print(i , ":", status_code_dict[i])
