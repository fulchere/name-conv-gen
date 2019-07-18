import time
import sys
if not sys.version_info >= (3,0):
    print("please run with python3")
    sys.exit()

pv_names = [("LS1-CA01-1","LS1_CA01:FTHS_N0001",0),("LS1-CA01-2","LS1_CA01:FTHS_N0002",0),("LS1-CA02-1","LS1_CA02:FTHS_N0001",0),("LS1-CA02-2","LS1_CA02:FTHS_N0002",0),("LS1-CA03-1","LS1_CA03:FTHS_N0001",0),("LS1-CA03-2","LS1_CA03:FTHS_N0002",0),("LS1-CB01","LS1_CB01:FTHS_N0001"),("LS1-CB01-CB02","LS1_CB01:FTHS_N0002"),("LS1-CB02","LS1_CB02:FTHS_N0001"),("LS1-CB03-1","LS1_CB03:FTHS_N0001 "),("LS1-CB03-2","LS1_CB03:FTHS_N0002",0),("LS1-CB04","LS1_CB04:FTHS_N0001 "),("LS1-CB04-CB05","LS1_CB04:FTHS_N0002"),("LS1-CB05","LS1_CB05:FTHS_N0001"),("LS1-CB06","LS1_CB06:FTHS_N0001"),("LS1-CB06-CB07","LS1_CB06:FTHS_N0002"),("LS1-CB07","LS1_CB07:FTHS_N0001"),("LS1-CB08","LS1_CB08:FTHS_N0001"),("LS1-CB08-CB09","LS1_CB08:FTHS_N0002"),("LS1-CB09","LS1_CB09:FTHS_N0001"),("LS1-CB10","LS1_CB10:FTHS_N0001"),("LS1-CB10-CB11","LS1_CB10:FTHS_N0002"),("LS1-CB11","LS1_CB11:FTHS_N0001"),("LS1-CC01-CC02","LS2_CC01:FTHS_N0102"),("LS1-CC03-CC04","LS2_CC03:FTHS_N0304"),("LS1-CC05-CC06","LS2_CC05:FTHS_N0506"),("LS1-CC07-CC08","LS2_CC07:FTHS_N0708"),("LS1-CC09-CC10","LS2_CC09:FTHS_N0910"),("LS1-CC11-CC12","LS2_CC11:FTHS_N1112")]
channels = ["A","B","C","D","E","F","G","H"]
channel_bool = False
attachments = [(".NAME","NAM_RD"),(".EGU","UNITS_RD"),("","T_RD"),(":SRDG","SEN_RD"),(".HIHI","HI_RD"),(".LOLO","LO_RD"),(".HIHI","HI_CSET"),(".LOLO","LO_CSET"),(".HIGH","HI_RD"),(".LOW","LO_RD"),(".HIGH","HI_CSET"),(".LOW","LO_CSET"),(".NAME","NAM_CSET"),(".EGU","UNITS_CSET")]

txt_file_pth = 'gen_conv_output'
num = 0
with open(txt_file_pth, 'w') as txtfile:
    for pv_name in pv_names:
        idstr = str(pv_name[0]+":ID,"+pv_name[1]+":ID_RD")
        print(num,idstr)
        num += 1
        txtfile.write(idstr+'\n')
        for channel in channels:
            if channel_bool and channel == "E":
                break
            for attachment in attachments:
                # OLD,NEW
                pair = str(pv_name[0]+":Ch"+channel+attachment[0]+","+pv_name[1]+":CH"+channel+attachment[1])
                print(num,pair)
                num += 1
                txtfile.write(pair+'\n') 
                #time.sleep(0.001)
txtfile.close()   


