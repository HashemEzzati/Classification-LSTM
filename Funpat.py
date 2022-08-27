

################**  Function1  **################
def Flen(T):
    return len(T)


################**  Function2  **################
def Fop(Ci):
    return Ci['Open']

################**  Function3  **################
def Fhp(Ci):
    return Ci['High']


################**  Function4  **################
def Flp(Ci):
    return Ci['Low']

################**  Function5  **################
def Fcp(Ci):
    return Ci['Close']


################**  Function6  **################
def Fhb(Ci):
    return abs(Ci['Close']-Ci['Open'])

################**  Function7  **################



################**  Function8  **################
def Ftp_body(Ci):
    return max(Ci['Close'],Ci['Open'])


################**  Function9  **################
def Fbm_body(Ci):
    return min(Ci['Close'],Ci['Open'])

################**  Function10  **################
def Fus(Ci):
    return Fhp(Ci) - Ftp_body(Ci)


################**  Function11  **################
def Fls(Ci):
    return Fbm_body(Ci) - Flp(Ci)



################**  Function12  **################
def Fhs(Ci):
    return Fus(Ci) + Fls(Ci)


################**  Function13  **################
def Fap(STC):
    return sum(STC)/len(STC)


################**  Function14  **################
def Fpt(TC,n):
    flag = 0
    firstFap = Fap(TC[0:n])
    for i in range( len(TC)-n ):
        if firstFap < Fap(TC[i+1:i+n+1]):
            firstFap = Fap(TC[i+1:i+n+1])
        else:
            flag = 1
            break
    if flag == 0: 
        return 1
    flag = 0
    firstFap = Fap(TC[0:n])
    for i in range( len(TC)-n ):
        if firstFap > Fap(TC[i+1:i+n+1]):
            firstFap = Fap(TC[i+1:i+n+1])
        else:
            flag = 1
            break
    if flag == 0:
        return -1
    return 0
        


################**  Function15  **################
def Fsli_greater(x, y,p):
    if 0.03*p <= ((x-y)/y)*100 < 0.1*p:
        return 1
    else: 
        return 0
    
    
################**  Function16  **################
def Fmod_greater(x, y,p):
    if 0.1*p <= ((x-y)/y)*100 < 0.25*p:
        return 1
    else: 
        return 0
    
    
################**  Function17  **################
def Flar_greater(x, y,p):
    if 0.25*p <= ((x-y)/y)*100 < 0.5*p:
        return 1
    else: 
        return 0


################**  Function18  **################
def Fext_greater(x, y,p):
    if ((x-y)/y)*100 >= 0.5*p:
        return 1
    else: 
        return 0


################**  Function19  **################
def Fsli_less(x, y,p):
    if 0.03*p <= ((y-x)/x)*100 < 0.1*p:
        return 1
    else: 
        return 0


################**  Function20  **################
def Fmod_less(x, y,p):
    if 0.1*p <= ((y-x)/x)*100 < 0.25*p:
        return 1
    else: 
        return 0
    

################**  Function21  **################
def Flar_less(x, y,p):
    if 0.25*p <= ((y-x)/x)*100 < 0.5*p:
        return 1
    else: 
        return 0

    
################**  Function22  **################    
def Fext_less(x, y,p):
    if  ((y-x)/x)*100 >= 0.5*p:
        return 1
    else: 
        return 0
    
################**  Function23  **################     
def Fext_near(x, y,p):
    if  (abs(y-x)/max(x,y))*100 <= 0.03*p:
        return 1
    else: 
        return 0    
    
################**  Function24  **################     
def Fmod_near(x, y,p):
    if  0.03*p <= (abs(y-x)/max(x,y))*100 < 0.1*p:
        return 1
    else: 
        return 0   


################**  Function25  **################ 
def Fnear(x, y,p):
    if  0*p <= (abs(y-x)/max(x,y))*100 < 0.1*p:
        return 1
    else: 
        return 0  


################**  Function26  **################ 
def Fnear_up(x, y,p):
    if 0.01*p <= ((y-x)/x)*100 < 0.03*p:
        return 1
    else: 
        return 0
    


################**  Function27  **################ 
def Fnear_down(x, y,p):
    if 0.01*p <= ((x-y)/y)*100 < 0.03*p:
        return 1
    else: 
        return 0


################**  Function28  **################ 




################**  Function29  **################





################**  Function30  **################
def FDoji(Ci,p):
    return Fext_near(Fop(Ci), Fcp(Ci),p)




################**  Function31  **################   
def Fsmall_body(Ci,p):
     return Fsli_less(Fbm_body(Ci), Ftp_body(Ci),p)

    
    
################**  Function32  **################
def Fnormal_body(Ci,p):
     return Fmod_less(Fbm_body(Ci), Ftp_body(Ci),p)
    

    
################**  Function33  **################    
def Flong_body(Ci,p):
     return Flar_less(Fbm_body(Ci), Ftp_body(Ci),p)

    
    
################**  Function34  **################
def Fel_body(Ci,p):
     return Fext_less(Fbm_body(Ci), Ftp_body(Ci),p)

    
################**  Function35  **################   
def Fno_us(Ci,p):
     return Fext_near(Fhp(Ci), Ftp_body(Ci),p)


    
################**  Function36  **################  
def Fsmall_us(Ci,p):
    return Fsli_greater(Fhp(Ci), Ftp_body(Ci),p)


################**  Function37  **################
def Fnormal_us(Ci,p):
    return Fmod_greater(Fhp(Ci), Ftp_body(Ci),p)



################**  Function38  **################
def Flong_us(Ci,p):
    return Flar_greater(Fhp(Ci), Ftp_body(Ci),p)



################**  Function39  **################
def Fel_us(Ci,p):
    return Fext_greater(Fhp(Ci), Ftp_body(Ci),p)



################**  Function40  **################
def Fno_ls(Ci,p):
    return Fext_near(Flp(Ci), Fbm_body(Ci),p)



################**  Function41  **################
def Fsmall_ls(Ci,p):
    return Fsli_less(Flp(Ci), Fbm_body(Ci),p)




################**  Function42  **################
def Fnormal_ls(Ci,p):
    return Fmod_less(Flp(Ci), Fbm_body(Ci),p)



################**  Function43  **################
def Flong_ls(Ci,p):
    return Flar_less(Flp(Ci), Fbm_body(Ci),p)



################**  Function44  **################
def Fel_ls(Ci,p):
    return Fext_less(Flp(Ci), Fbm_body(Ci),p)



################**  Function45  **################
def Fblack_body(Ci):
    if Fop(Ci) > Fcp(Ci):
        return 1
    else:
        return 0



################**  Function46  **################
def Fwhite_body(Ci):
    if Fop(Ci) < Fcp(Ci):
        return  1
    else:
        return 0



################**  Function47  **################
def Fsmall_black_body(Ci,p):
    return Fsmall_body(Ci,p) and Fblack_body(Ci)
    
    
    
################**  Function48  **################
def Fsmall_white_body(Ci,p):
    return Fsmall_body(Ci,p) and Fwhite_body(Ci)
    

    
################**  Function49  **################    
def Fnormal_black_body(Ci,p):
    return Fnormal_body(Ci,p) and Fblack_body(Ci)



################**  Function50  **################
def Fnormal_white_body(Ci,p):
    return Fnormal_body(Ci,p) and Fwhite_body(Ci)
    
    
    
################**  Function51  **################
def Flong_black_body(Ci,p):
    return Flong_body(Ci,p) and Fblack_body(Ci)
    

    
################**  Function52  **################    
def Flong_white_body(Ci,p):
    return Flong_body(Ci,p) and Fwhite_body(Ci)
    
    
    
################**  Function53  **################
def Fel_black_body(Ci,p):
    return Fel_body(Ci,p) and Fblack_body(Ci)



################**  Function54  **################
def Fel_white_body(Ci,p):
    return Fel_body(Ci,p) and Fwhite_body(Ci)


################**  Function57  **################  
def Fdown_body_gap(Ci,Cj):
    if Fbm_body(Ci) > Ftp_body(Cj):
        return 1
    else:
        return 0
    
    
    
    
    
#########################**  Patterns  **##########################




#########################**  Pattern1  **##########################
def MarubozuBlack(S,Ci,p):
    if Flen(S)==1 and Fno_us(Ci,p) and Flong_black_body(Ci,p) and Fno_ls(Ci,p):
        return 1
    else:
        return 0

    
#########################**  Pattern2  **##########################
def MarubozuWhite(S,Ci,p):
    if Flen(S)==1 and Fno_us(Ci,p) and Flong_white_body(Ci,p) and Fno_ls(Ci,p):
        return 1
    else:
        return 0    

#########################**  Pattern3  **##########################
def BeltHoldBullish(S,TC,Ci,n,p):
    if Flen(S)==1 and (Fpt(TC,n) == -1) and Fnormal_white_body(Ci,p) and Fno_ls(Ci,p) and Fmod_near(Fcp(Ci), Fhp(Ci),p):
        return 1
    else:
        return 0    
    
    
    
#########################**  Pattern4  **##########################
def MarubozuClosingBlack(S,Ci,p):
    if Flen(S)==1 and  Fnormal_black_body(Ci,p) and not Fno_us(Ci,p) and Fno_ls(Ci,p):
        return 1
    else:
        return 0    


#########################**  Pattern5  **##########################
def MarubozuOpeningWhite(S,Ci,p):
    if Flen(S)==1 and  Fnormal_white_body(Ci,p) and not Fno_us(Ci,p) and Fno_ls(Ci,p):
        return 1
    else:
        return 0    
    
    
    
#########################**  Pattern6  **##########################    
def ShootingStarOneCandle(S,TC,Ci,n,p):
    if Flen(S)==1  and  (Fpt(TC,n) == 1) and Fnormal_us(Ci,p)  and (Fus(Ci) > 2*Fhb(Ci))   and Fsmall_body(Ci,p) and Fno_ls(Ci,p):
        return 1
    else:
        return 0
    

#########################**  Pattern7  **##########################        
def DojiGravestone(S,Ci,p):
    if Flen(S)==1 and  FDoji(Ci,p) and Fno_ls(Ci,p) and Fnormal_us(Ci,p):
        return 1
    else:
        return 0        
    
    
#########################**  Pattern8  **##########################    
def BeltHoldBearish(S,TC,Ci,n,p):
    if Flen(S)==1  and  (Fpt(TC,n) == 1) and Fno_us(Ci,p)  and Fsmall_ls(Ci,p) and Fnormal_black_body(Ci,p):
        return 1
    else:
        return 0



#########################**  Pattern9  **########################## 
def DojiDragonfly(S,Ci,p):
    if Flen(S)==1 and  FDoji(Ci,p) and Fsmall_us(Ci,p) and Flong_ls(Ci,p):
        return 1
    else:
        return 0   


    
#########################**  Pattern10  **##########################     
def Hammer(S,TC,Ci,n,p):
    if Flen(S)==1 and  (Fpt(TC,n) == -1) and Fsmall_body(Ci,p) and not(Fno_ls(Ci,p)) and (2*Fhb(Ci) < Fls(Ci) and Fls(Ci) < 3*Fhb(Ci)) and (Fsmall_us(Ci,p) or Fno_us(Ci,p)):
        return 1
    else:
        return 0
    
#########################**  Pattern11  **##########################
def HangingMan(S,TC,Ci,n,p):
    if Flen(S)==1  and  (Fpt(TC,n) == 1) and Fno_us(Ci,p)  and Fsmall_body(Ci,p) and Flong_ls(Ci,p):
        return 1
    else:
        return 0

    

#########################**  Pattern12  **########################## 
def MarubozuOpeningBlack(S,Ci,p):
    if Flen(S)==1 and  Fnormal_black_body(Ci,p) and not Fno_ls(Ci,p) and Fno_us(Ci,p):
        return 1
    else:
        return 0      

    
    
#########################**  Pattern13  **########################## 
def MarubozuClosingWhite(S,Ci,p):
    if Flen(S)==1 and  Fnormal_white_body(Ci,p) and Fno_us(Ci,p) and not Fno_ls(Ci,p):
        return 1
    else:
        return 0  
    


#########################**  Pattern14  **##########################
def TakuriLine(S,TC,Ci,n,p):
    if Flen(S)==1  and  (Fpt(TC,n) == -1) and Fsmall_body(Ci,p) and Fno_us(Ci,p) and (Fls(Ci) > (3*Fhb(Ci))):
        return 1
    else:
        return 0


    
#########################**  Pattern44  **##########################
def HammerInverted(S,TC,Ci,Cj,n,p):
    if Flen(S)==2  and  (Fpt(TC,n) == -1) and Flong_black_body(Ci,p) and Fsmall_ls(Ci,p) and Fsmall_body(Cj,p) and Flong_us(Cj,p) and Fno_ls(Cj,p) and Fdown_body_gap(Ci,Cj):
        return 1
    else:
        return 0    