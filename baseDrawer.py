#Input Values
xHeight = 500
ascender = 750
descender = 250
capHeight = 720
baselineOverShoot = 15
xHeightOverShoot = 15 


#Calcs    
baseline = 220
equis = (xHeight/10)*2.8346
ascendente = (ascender/10)*2.8346
descendente = (descender/10)*2.8346
mayusculas = (capHeight/10)*2.8346
baseOvershoot = (baselineOverShoot/10)*2.8346
xOvershoot = (xHeightOverShoot/10)*2.8346

#Texts
page = newPage('A4Landscape')
font("Menlo")
fontSize(8)

text("base.(0)", (30, baseline-2))
text("x–h(" +  str(xHeight) + ")", (30, (baseline+equis)-2))
text("asc.(" +  str(ascender) + ")", (30, (baseline+ascendente)-2))
text("cap.(" +  str(capHeight) + ")", (30, (baseline+mayusculas)-2))
text("desc.(" +  str(descender) + ")", (30, (baseline-descendente)-2))
text("1cm ≈ 100 upm", (30, 30))

font("Menlo-Bold")
text("Project Name:", (30, 540))
text("Style:", (30, 525))
text("Weight:", (30, 510))
text("Date:", (30, 495))

strokeWidth(0.4)
stroke(0, 0, 0)
end = width()

#Drawings

line((85, baseline), (end-30, baseline))#Baseline

line((85, baseline+equis), (end-30, baseline+equis))#AlturaX

line((85, baseline+ascendente), (end-30, baseline+ascendente))#ascender

line((85, baseline-descendente), (end-30, baseline-descendente))#descender

line((85, baseline+mayusculas), (end-30, baseline+mayusculas))#cap height


fill(1, 0, 0, .2)
strokeWidth(0)

rect(85, baseline, end-85-30, -xOvershoot) #BaselineOvershoot

rect(85, baseline+equis, end-85-30, xOvershoot)#xHeightOverShoot

saveImage("~/Desktop/base.pdf")