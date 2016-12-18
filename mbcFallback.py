#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tapon
#
# Created:     12/11/2013
# Copyright:   (c) tapon 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import MySQLdb
import sys
import os


def main():
    bts_name = raw_input("ENTER BTS NAME : ")
    bcch_arfcn = raw_input("ENTER BCCH ARFCN : ")
    DBoperation(bts_name,bcch_arfcn)
    pass

def DBoperation(btsName,bcchArfcn):
    bts_name = btsName
    BCCH = bcchArfcn
    db = MySQLdb.connect('localhost','root','','myflexml')
    cursor = db.cursor()
    cmd = "SELECT bsc,bcf,bts,segmentid,locationareaidlac,cellid,rac,nsei,bsidentitycodebcc,bsidentitycodencc FROM bts where name like\"%"+bts_name+"%\";"
    print cmd
    cursor.execute(cmd)
    data = cursor.fetchall()



    row = data[0]

    BSC = row[0]
    BCF = row[1]
    BTS = row[2]
    SEG = row[3]
    LAC = row[4]
    CI = str(int(row[5])+3)
    RAC = row[6]
    NSEI = row[7]
    BCC = row[8]
    NCC= row[9]

    print "BSC:\t"+BSC
    print "BCF:\t"+BCF
    print "BTS:\t"+BTS
    print "SEG:\t"+BTS
    print "CELLID:\t"+LAC+"-"+CI

    cursor.execute("select trx,initialfrequency,tsc,channel0pcm,lapdLinkName,channel0tsl from trx WHERE BSC="+BSC+" and BCF="+BCF+" and BTS="+BTS+";")
    data_trx = cursor.fetchall()
    TRX=[]
    ARFCN=[]
    TSC=[]
    PCM=[]
    LAPD=[]
    FTSL=[]
    for row in data_trx:
        TRX.append(row[0])
        ARFCN.append(row[1])
        TSC.append(row[2])
        PCM.append(row[3])
        LAPD.append(row[4])
        FTSL.append(row[5])

    fp = open("C:\\mbc_out.txt","w+")
    fp.writelines("ZEEI:BCF="+BCF+";\n")
    fp.writelines("ZERO:BTS="+BTS+";\n")
    for pcm in PCM:
        fp.writelines("ZDSB:::PCM="+pcm+";\n")
    fp.writelines("Stop\n")
    fp.writelines("ZEQS:BTS="+BTS+":L;\n")
    fp.writelines("ZEQD:BTS="+BTS+"; Y\n")
    fp.writelines("ZEQC:BCF="+BCF+",BTS="+BTS+",NAME="+bts_name+",SEG="+BTS+",SEGNAME="+bts_name+":CI="+CI+",BAND=1800:NCC="+NCC+",BCC="+BCC+":MCC=470,MNC=03,LAC="+LAC+"::GENA=Y,RAC="+RAC+",NSEI="+NSEI+":;\n")
    fp.writelines("ZEUC:SEG="+BTS+":;\n")
    fp.writelines("ZEHC:SEG="+BTS+":;\n")
    fp.writelines("ZEQA:BTS="+BTS+":MAL=0,MO=0,MS=2,:;\n")
    fp.writelines("ZEQF:SEG="+BTS+":BAR=Y,RE=N,EC=N,PLMN=0&&7,DR=Y,DRM=1,MADR=6,MIDR=0,;\n")
    fp.writelines("ZEQG:SEG="+BTS+":HYS=6,RXP=-104,RLT=32,PRC=6,;\n")
    fp.writelines("ZEQJ:SEG="+BTS+":MFR=2,PER=5,AG=1,ATT=Y,;\n")
    fp.writelines("ZEQM:SEG="+BTS+":DTX=1,NY1=35,SLO=10,CB=Y,BLT=80,DMAX=62,FRL=80,FRU=90,MBR=2,TRP=2,TRIH=0,AUT=100,TGT=10,AML=0,RET=4,ESI=Y::QUA=N,TEO=0,PI=Y,REO=0,PET=20;\n")
    fp.writelines("ZEQM:BTS="+BTS+":RDIV=Y,NBL=0,LSEG=40;\n")
    fp.writelines("ZEQV:SEG="+BTS+":BFG=1,MCU=5,MCA=6,ELA=2;\n")
    fp.writelines("ZEQV:BTS="+BTS+":EGENA=N,CDED=10,CDEF=10,CMAX=100,CS34=N,DCSU=5,DCSA=5,UCSU=5,UCSA=5,ALA=Y;\n")
    fp.writelines("ZEQY:BTS="+BTS+":FRC=1&4&32&128,HRC=1&4&16;\n")
    fp.writelines("ZEQY:SEG="+BTS+":ARLT=36;\n")
    fp.writelines("ZEQK:BTS="+BTS+":BO1=-107,BO2=-103,BO3=-97,BO4=-87,CNT=20;\n")
    fp.writelines("ZEQK:SEG="+BTS+":AP=31;\n")
    fp.writelines("ZEUB:BTS="+BTS+":UDRF=1,UURF=1,UDRH=1,UURH=1,LDRF=3,LURF=3,LDRH=3,LURH=3:;\n")
    fp.writelines("ZEHB:BTS="+BTS+":QDRF=6,QURF=6,QDRH=5,QURH=5,IHRF=3,IHRH=5;\n")
    fp.writelines("ZEQY:BTS="+BTS+"::FRS=01,FRI=0,FRTD1=12,FRTD2=17,FRTD3=25,FRTU1=8,FRTU2=14,FRTU3=22,FRH1=2,FRH2=3,FRH3=3,HRS=1,HRI=0,HRTD1=23,HRH1=3,HRTD2=30,HRH2=4,HRTD3=0,HRH3=0,HRTU1=22,HRTU2=28,HRTU3=0,:;\n")
    fp.writelines("ZEUA:SEG="+BTS+":LDS=4,LUS=4,LDW=2,LUW=2,QDS=2,QDW=2,QUS=2,QUW=2:;\n")
    fp.writelines("ZEUS:SEG="+BTS+":UDR=-80,UDP=1,UDN=1,UUR=-85,UUP=1,UUN=1,LDR=-85,LDP=1,LDN=1,LUR=-92,LUP=1,LUN=1:;\n")
    fp.writelines("ZEUQ:SEG="+BTS+":UDR=1,UDP=2,UDN=3,UUR=1,UUP=2,UUN=3,LDR=3,LDN=3,LDP=2,LUR=3,LUN=3,LUP=2;\n")
    fp.writelines("ZEUG:SEG="+BTS+":PENA=Y,PMAX1=0,PMAX2=0,PMIN=30,INC=6,RED=2,INT=2,PD0=38,PD1=38,PD2=38,PDF=1;\n")
    fp.writelines("ZEUM:SEG="+BTS+":IFP=9,TFP=13,:;\n")
    fp.writelines("ZEHG:SEG="+BTS+":EIC=Y,EIH=Y,EPB=Y,EMS=Y,ESD=N,EUM=N,EFH=N,MIH=10,MIU=15,HPP=8,HPU=6,ATPM=N;\n")
    fp.writelines("ZEHA:SEG="+BTS+":LDWS=8,LDW=2,LUWS=8,LUW=2,QDWS=6,QDW=2,QUWS=6,QUW=2,;\n")
    fp.writelines("ZEHS:SEG="+BTS+":LDR=-98,LDP=3,LDN=4,LUR=-100,LUP=3,LUN=4,LAR=-85,LER=-96,LEP=3,LEN=4:;\n")
    fp.writelines("ZEHQ:SEG="+BTS+":QDR=5,QDP=4,QDN=6,QUR=5,QUP=4,QUN=6:;\n")
    fp.writelines("ZEHI:SEG="+BTS+":IDR=-77,IDP=3,IDN=4,IUR=-82,IUP=3,IUN=4;\n")
    fp.writelines("ZEHD:SEG="+BTS+":MSWS=8,MSR=63,MSP=1,MSN=1;\n")
    fp.writelines("ZEHN:SEG="+BTS+":AWS=6,NOZ=2,AAC=N;\n")
    fp.writelines("ZEHY:SEG="+BTS+":CGR=-76,CBR=-94;\n")
    fp.writelines("ZEHP:SEG="+BTS+":LSL=0,USL=0,STP=3,STN=6,SDS=0;\n")
    fp.writelines("ZEHB:SEG="+BTS+":LLLAMR=-70,ULLAMR=-47,LQLAMR=5;\n")
    fp.writelines("ZEQH:SEG="+BTS+":MQL=50,TLC=6,TLH=0,QPU=Y,QPC=7,QPH=9,QPN=9,MPU=N,;\n")

    DAP = []
    DAP_PCM = []
    cursor.execute("Select trx,dapool_id,channel0pcm from trx where bsc=247039 and bcf=67;")
    data_dap = cursor.fetchall()
    for row in data_dap:
        if row[1] not in DAP and row[1]!='65535':
            DAP.append(row[1])
        if row[2] not in DAP_PCM and row[1]!='65535':
            DAP_PCM.append(row[2])
    dapid = DAP[0]
    dappcm =DAP_PCM[0]

    #print "DAP PCM: "+dappcm

    for trx in TRX:
        if ARFCN[TRX.index(trx)]==BCCH:
            print "TRX PCM="+PCM[TRX.index(trx)]
            if dappcm == PCM[TRX.index(trx)]:
                fp.writelines("ZERC:BTS="+BTS+",TRX="+trx+":PREF=,GTRX=Y,DAP=,:FREQ="+ARFCN[TRX.index(trx)]+",TSC="+BCC+",PCMTSL="+PCM[TRX.index(trx)]+"-"+FTSL[TRX.index(trx)]+":DNAME="+LAPD[TRX.index(trx)]+":CH0=MBCCH,CH1=SDCCB,CH2=TCHD,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD,::;\n")
                fp.writelines("ZERM:BTS="+BTS+",TRX="+trx+":DAP="+dapid+";\n")
                print "TRX PCM: "+PCM[TRX.index(trx)]
            else:
                fp.writelines("ZERC:BTS="+BTS+",TRX="+trx+":PREF=,GTRX=N,DAP=,:FREQ="+ARFCN[TRX.index(trx)]+",TSC="+BCC+",PCMTSL="+PCM[TRX.index(trx)]+"-"+FTSL[TRX.index(trx)]+":DNAME="+LAPD[TRX.index(trx)]+":CH0=MBCCH,CH1=SDCCB,CH2=TCHD,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD,::;\n")
                print "ATTENTION!! TRX PCM("+PCM[TRX.index(trx)]+") and DAP PCM("+dappcm+") mismatch, Dap cannot be assigned"
            continue
        fp.writelines("ZERC:BTS="+BTS+",TRX="+trx+":PREF=,GTRX=N,DAP=,:FREQ="+ARFCN[TRX.index(trx)]+",TSC="+BCC+",PCMTSL="+PCM[TRX.index(trx)]+"-"+FTSL[TRX.index(trx)]+":DNAME="+LAPD[TRX.index(trx)]+":CH0=TCHD,CH1=TCHD,CH2=TCHD,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD,::;\n")
    for trx in TRX:
        fp.writelines("ZERS:BTS="+BTS+",TRX="+trx+":U;\n")
    fp.writelines("ZEQS:BTS="+BTS+":U;")



    fp.close()
    cursor.close()
    db.commit()
    os.startfile("C:\\mbc_out.txt")

if __name__ == '__main__':
    main()
