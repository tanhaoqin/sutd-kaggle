with open("train.csv","r") as infile, open("output.csv","w") as outfile:
	count = 0
	for line in infile:
		if count ==0:
			outfile.write("No,CC,GN,NS,BU,FA,LD,BZ,FC,FP,RP,PP,KA,SC,TS,NV,MA,LB,AF,HU,Price,Choice\n")
			count+=1
			continue
		row = line.split(",")
		Case,No,Task,CC1,GN1,NS1,BU1,FA1,LD1,BZ1,FC1,FP1,RP1,PP1,KA1,SC1,TS1,NV1,MA1,LB1,AF1,HU1,Price1 = row[0:23]
		CC2,GN2,NS2,BU2,FA2,LD2,BZ2,FC2,FP2,RP2,PP2,KA2,SC2,TS2,NV2,MA2,LB2,AF2,HU2,Price2 = row[23:43]
		CC3,GN3,NS3,BU3,FA3,LD3,BZ3,FC3,FP3,RP3,PP3,KA3,SC3,TS3,NV3,MA3,LB3,AF3,HU3,Price3 = row[43:63]
		CC4,GN4,NS4,BU4,FA4,LD4,BZ4,FC4,FP4,RP4,PP4,KA4,SC4,TS4,NV4,MA4,LB4,AF4,HU4,Price4 = row[63:83]
		segment,year,miles,night,gender,age,educ,region,Urb = row[83:92]
		income = row[92:len(row)-6]
		ppark,Ch1,Ch2,Ch3,Ch4,Choice = row[-6:]
		outfile.write(",".join([str(count),CC1,GN1,NS1,BU1,FA1,LD1,BZ1,FC1,FP1,RP1,PP1,KA1,SC1,TS1,NV1,MA1,LB1,AF1,HU1,Price1,Ch1])+"\n")
		outfile.write(",".join([str(count+1),CC2,GN2,NS2,BU2,FA2,LD2,BZ2,FC2,FP2,RP2,PP2,KA2,SC2,TS2,NV2,MA2,LB2,AF2,HU2,Price2,Ch2])+"\n")
		outfile.write(",".join([str(count+2),CC3,GN3,NS3,BU3,FA3,LD3,BZ3,FC3,FP3,RP3,PP3,KA3,SC3,TS3,NV3,MA3,LB3,AF3,HU3,Price3,Ch3])+"\n")
		outfile.write(",".join([str(count+3),CC4,GN4,NS4,BU4,FA4,LD4,BZ4,FC4,FP4,RP4,PP4,KA4,SC4,TS4,NV4,MA4,LB4,AF4,HU4,Price4,Ch4])+"\n")
		count+=4
		