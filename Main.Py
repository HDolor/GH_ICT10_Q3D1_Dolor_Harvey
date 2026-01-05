from pyscript import display, document 
def gwa(es):
    document.getElementById('av').innerHTML=" "
    document.getElementById('gw').innerHTML=" "
    fn=document.getElementById('fn').value
    ln=document.getElementById('ln').value
    sn=document.getElementById('sn').value
    gs=document.getElementById('gs').value
    sc=int(document.getElementById('sc').value)
    en=int(document.getElementById('en').value)
    ic=int(document.getElementById('ic').value)
    ma=int(document.getElementById('ma').value)
    fi=int(document.getElementById('fi').value)
    pe=int(document.getElementById('pe').value)
    su=["Science", "English", "ICT", "Math", "Filipino", "PE"]
    un=(1, 2, 3, 4, 5)
    display(f'{fn} {ln}', target="av")
    display(f'{sn}\n {gs}', target="av")
    display(f'{su[0]} : {sc}', target="av")
    display(f'{su[1]} : {en}', target="av")
    display(f'{su[2]} : {ic}', target="av")
    display(f'{su[3]} : {ma}', target="av")
    display(f'{su[4]} : {fi}', target="av")
    display(f'{su[5]} : {pe}', target="av")
    scun=sc*un[4]
    enun=en*un[4]
    icun=ic*un[1]
    maun=ma*un[4]
    fiun=fi*un[2]
    peun=pe*un[0]
    tot=scun+enun+icun+maun+fiun+peun
    toun=un[4]+un[4]+un[4]+un[1]+un[2]+un[0]
    gwa=tot/toun
    gwa=round(gwa, 2)
    if gwa > 74: #More than 74
        display(f'PASSED', target="gw")
    else: #Less than 75
        display(f'FAILED', target="gw")
    display(f'Your General Weight Average is: {gwa}', target='gw')
