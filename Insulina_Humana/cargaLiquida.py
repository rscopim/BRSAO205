preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

lsInsulina = "malwmrllpllallalwgpdpaaa"  
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulina = "giveqcctsicslyqlenycn"  
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulina = bInsulina + aInsulina

pKR = {
    'y':10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25,
}
print("\nDicionário pKR.")
print(pKR)
print("\nContando o Y:")
print("quantidade de Y: ", float(insulina.count("y")))
seqContar = {x: float(insulina.count(x)) for x in ['y','c','k','h','r','d','e']}
print("\n")
print(seqContar)
print("\n")

pH = 0
while (pH <= 14):
    cargaLiquida = (
        +(sum({x: ((seqContar[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x])))
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqContar[x]*(10**pH))/((10**pH)+(10**pKR[x])))
        for x in ['y','c','d','e']}.values()))
    )
    print("pH:", '{0:2f}'.format(pH), " Carga líquida: ", cargaLiquida)
    pH += 1