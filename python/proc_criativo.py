#!/usr/bin/python3
# -*- coding: utf-8 -*-

import proc_criatividade as criatividade
 
from  dao.cenario       import      Cenario  
from  dao.perssonagem   import      Perssonagem  
from  dao.objeto        import      Objeto
from  dao.transporte    import      Transporte
from  dao.missao        import      Missao
from  dao.textos        import      Textos
from  dao.jogador       import      Jogador 
from  dao.acoes         import      Acoes
 
 #  cenario     ok    
 #  perssonagem ok
 #  objeto      ok
 #  transporte  ok
 #  missao      ok
 #  narrativa   ok
 
    ## SQl para a pergunta 1
    ##select * from log_jogo
    ##where  data between
    ##(select data_inicio from aplicacoes where aplicacao=2) and
    ##(select data_fim from aplicacoes where aplicacao=2) and
    ##pag_acessada='https://www.omundodanarrativa.com.br/iniciodo' and
    ##id_pessoa=11
 
 
def resultado_criatividade(pontos):
    # print("total de pontos: ", resultado)
    if pontos < 30:
        resultado_final = "pouco criativo(a)"
    if  pontos >=30 or pontos <=70:
            resultado_final = "potencial criativo(a)"
    if  pontos >70:
            resultado_final = "criativo(a)"
            
    return resultado_final
    
 
 
 
 
def AnalizaCriatividade(id_pessoa):
    cenario=Cenario()
    perssonagem=Perssonagem()
    objeto=Objeto()
    tranpporte=Transporte()
    missao=Missao()
    texto=Textos()
    acoes = Acoes()
    jogador =Jogador()

    cena= cenario.getCenario(id_pessoa)
    perso= perssonagem.getPersonagem(id_pessoa)
    ojb= objeto.getobjeto(id_pessoa)
    tranp= tranpporte.getTransporte(id_pessoa)
    mis= missao.getMissao(id_pessoa)
    tx = texto.busca_processamento(id_pessoa,"2")
    jog = jogador.getJogador(id_pessoa)
     
    FezMaisUmaJogada=0
    FezMAisUmElemento=0
    CriouProprioElemento=0
    EscolheCombIncomum=0
    PersonagemAbs=0
    IniciouSelecao=0
    PreencheuTudo=0
    FinalFeliz = 0
    VacaSaltadora = 0
    QuebraParadigma=0
    Flexibilidade = 0
    
    SomaMaisUmaJogada=0
    SomaMAisUmElemento=0
    
    if(criatividade.buscaGeral(id_pessoa)):
        EscolheCombIncomum=10
        
    soma=0
    for c in cena:
        soma+=1
        if(c.objcenario=="coringa"):
            CriouProprioElemento=10
        soma+=1
    if(soma>1):
        FezMAisUmElemento=10
    
    
    
    soma=0    
    for p in perso:
        if(p.tipo_personagem=="frutas" or p.tipo_personagem=="legumes" or p.tipo_personagem=="animais"or p.tipo_personagem=="arvores"):
            PersonagemAbs=10
            
        if(p.tipo_personagem=="coringa"):
            CriouProprioElemento=10
        soma+=1
    if(soma>1):
        FezMAisUmElemento=10
    
    
    
    
    soma=0
    for o in ojb:
        
        if(o.objselecao=="caixamagica"):
            CriouProprioElemento=10
        soma+=1
    if(soma>1):
        FezMAisUmElemento=10
    
    
    
    
    soma=0    
    for t in tranp:
        soma+=1
    if(soma>1):
        FezMAisUmElemento=10    
    

    
    soma=0    
    for m in mis:
        if(m.biscoito=="Biscoito 3" or m.biscoito=="Biscoito 13" or m.biscoito=="Biscoito 15"):
            QuebraParadigma=10
        if(m.finalfeliz=="n"):
            FinalFeliz=10
        if(m.biscoito=="Biscoito 15"):
            CriouProprioElemento=10

        soma+=1
    if(soma>1):
        FezMAisUmElemento=10    
    
    
    
    soma=0    
    for t in tx:
        soma+=1
    if(soma>1):
        FezMaisUmaJogada=10   
  
    #print("aqui"+jog)
    for  j in jog:
        if(j.fluencia!=None or j.fluencia!=""):
            PreencheuTudo=10
            
        if(j.adaptacao!=None or j.adaptacao!=""):
            Flexibilidade=10
            
      
    ac = acoes.carrega(id_pessoa,"direcao")  
    if(ac[0].acao=="escolheu ir para o fasemissao" or  ac[0].acao=="escolheu ir para o fasemissao"):
        IniciouSelecao=10
        

    total=FezMaisUmaJogada+FezMAisUmElemento+CriouProprioElemento+EscolheCombIncomum+PersonagemAbs+IniciouSelecao+PreencheuTudo+FinalFeliz+VacaSaltadora+QuebraParadigma+Flexibilidade+SomaMaisUmaJogada+SomaMAisUmElemento
 
    respostas=str(total)+" - "+resultado_criatividade(total)
    print(respostas)
    jog =Jogador()
    jog.id_pessoa=id_pessoa
    jog.criatividade=respostas
    jog.cadCriatividade()   
    