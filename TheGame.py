#!/usr/bin/env python3

#VUOI GIOCARE?

start= input('vuoi giocare? ')
lettera = 0
suggerimento = 3
chiave = 0
fine = 0
j = 0
if start=='si' or start==' si':
    #rogole
    print('                                         REGOLE DEL GIOCO')
    print('               dopo una domanda risopondi scrivendo \'si\' o \'no\' se richiesto e premi INVIO ')
    print('               altrimenti digita l\'alternativa che scegli nella maniera piu\' completa possibile e premi INVIO ')
    print('               se compare \n               ...\n               premi INVIO ')
    print('               puoi usare 3 suggerimenti se ritieni necessario, hai 5 tentativi per ogni enigma')
    print('               buon divertimento!')
    input('...')
    #INTRODUZIONE
    print('Sei un\'uomo di 32 anni. La tua storia e\' cominciata nel collegio delle suore,')
    print('essendo orfano hai sempre dovuto affrontare la vita da solo,')
    print('e fino ad adesso la tua esistenza non ti ha condotto da nessuna parte...')
    input('...')
    print('ma dove ti trovi adesso? sei sdraiato su una brandina, c\'e\' una piccola luce che rischiara la stanza')
    print('cerchi di pensare all\'ultima cosa che ricordi... stavi passeggiando quando sentisti una puntura di un insetto sul collo')
    print('e poi piu\' niente. Devono averti narcotizzato, senti ancora un leggero mal di testa')
    input('...')
    print('devi pensare a quale sara\' la tua prossima mossa')
    #prima scelta
    s1 = input('inizi a urlare nella speranza che qualcuno ti senta o ti alzi e ispezioni la stanza?')
    if s1.find('urlare')>0 or s1.find('rl')>0  :
        print('non sembra che hai risolto nulla...')
        s1 = input('e adesso? ')
    if s1.find('tanza')>0 or s1.find('ispez')>0  or s1.find('lzo')>0 :
        print('nella stanza trovi una scrivania con una lettera sopra, uno specchio e ovviamente una porta')
        #seconda scelta
        s2= input('dove vai? ')
        #se guardi nello specchio
        if s2.find('pecchio')>0:
            print('ti guardi allo specchio, subito ti accorgi di avere una scritta sulla fronte,')
            print('\'5890\'')
            print('per fortuna e\' pennarello, con un o\' di frizione riesci a cancellarla')
            #decidi o porta o lettera
            s2= input('dove vai adesso? ')
        if s2.find('crivania')>0 or s1.find('ettera')>0 :
            print('leggi la lettera...')
            input('...')
            print('             Adorata Molly,')
            print('             mi continuavi a chiedere quale fosse il regalo che stavo preparando con tanta cura')
            print('             per il tuo undicesmo compleanno. E\' finalmente arrivato l\'ora che tu lo sappia.')
            print('             Ho creato per te il piu\'difficile e complesso percorso ad enigmi che abbia mai fatto')
            print('             i giochi che ti facevo quando eri piu\' piccola sono niente in confronto.')
            print('             Spero che ti piaccia, buon compleanno tesoro!')
            print('             il tuo vecchio padre \n')
            print('             p.s. non scordarti mai che niente e\' impossibile')
            input('...')
            s2= input('adesso vai verso lo specchio o esci dalla porta? ')
            if s2.find('pecchio')>0:
                print('ti guardi allo specchio, subito ti accorgi di avere una scritta sulla fronte,')
                print('\'5890\'')
                print('per fortuna e\' pennarello, con un po\' di frizione riesci a cancellarla')
                s2 = ' porta'
            #vai alla porta
        if s2.find('orta')>0 or s2.find('sco')>0:
            print('adesso apri la porta, sembra che dia su un corridoio buio...')
            #scegli se accendere la luce
            s3= input('provi ad accendere la luce? ')
            if s3 == 'no':
                print('ok, peccato che non sei un felino con la visione notturna... meglio se accendi la luce!')
                s3 ='si'
            if s3=='si' or s3==' si':
                print('ok, adesso puoi vedere che nel corridoio si affacciano due porte e una rampa di scale che porta al piano inferiore... \nnon deve essere un piccolo edificio')
                input('...')
                # provi le porte o scendi le scale?
                s4= input('provi ad aprire le porte o scedi le scale? ')
                if s4.find('ort')>0:
                    print('una porta e\' chiusa a chiave, mentre l\'altra e\' aperta')
                    #che fai entri o no?
                    s5 =input('entri?')
                    if s5 =='si' or s5==' si':
                        print('sei detro, ti giri intorno, vedi solamente un piccolo armadio, una poltrona davanti ad un camino spento,')
                        print('un trepiedi da pittore con un sgabello vicino e colori ad olio ormai secchi e pennelli vari')
                        #esci frughi o ti siedi?
                        s6= input('esci, ti metti a frugare nella stanza in cerca di risposte \no ti siedi un attimo sulla poltrona a riflettere? ')
                        if s6.find ('poltrona')>0 or s6.find('riflett')>0 or s6.find('sedere')>0 or s6.find('siedo')>0:
                            print('stai veramente comodo in questa poltrona...')
                            input('...')
                            input('...')
                            input('...')
                            input('...')
                            print('ti stavi quasi per riaddormentare quando la tua attenzione e\'stata catturata dai numerosi ritratti appesi alle pareti')
                            input('...')
                            print('ti alzi dalla poltrona e ti avvicini ai dipinti...')
                            input('...')
                            print('ti accorgi che sono tutti dello stesso soggetto')
                            print('probabilmente si tratta della bambina della lettera...')
                            print('c\'e\' un ritratto per ogni anno, deve averli fatti una person che l\'amava molto')
                            input('...')
                            print('accanto alla data in basso a sinistra c\'e anche la firma \'Evelin\'')
                            print('forse e\' la madre...')
                            s6=input('esci o ti metti a frugare nella stanza?')
                        if s6.find ('ru')>0:
                            print('sembra tutto cosi\'impolverato, non deve essere stata aperta da molto questa stanza...')
                            print('nell\'armadio ci sono solo vecchi stracci ed altri colori ad olio')
                            print('aspetta un momento, cos\'e\' questo?')
                            input('...')
                            print('c\'e\' un piccolo foglio di carta in mezzo ai pennelli, ci sono poche righe scritte a penna....')
                            print('        Sono colei che prima entra e poi apre, hai bisogno di me')
                            print('        Sono in mezzo a cio che quando si compra e\' nero, quando lo usi rosso e quando diventa inutile e\' bianco')
                            input('...')
                            #risolvi l'indovinello prima parte
                            for i in range(0,5):
                                #suggerimento
                                if i == 2 :
                                    s20= input('vuoi un suggerimento?')
                                    if s20 == 'si':
                                        suggerimento= suggerimento-1
                                        print('serve per aprire le porte...')
                                s7= input('cosa devi cercare? ')

                                if  s7.find('hiave')>0:
                                  print('ci siamo!')
                                   #risolvi l'indovinello seconda parte
                                  for j in range(0,5):

                                      if j == 2 :
                                          s20= input('vuoi un suggerimento?')
                                          if s20 == 'si':
                                             suggerimento = suggerimento -1
                                             print('e\' una cosa presente nella stanza...')
                                      s8= input('Dove devi cercarla? ')
                                      if s8.find('amin')>0 or s8.find('uoco')>0 or s8.find('amin')>0 or s8.find('egn')>0 or s8.find('enere')>0 or s8.find('arbon')>0:
                                          print('ti avvicini al caminetto, inizi a smuovere la cenere... ')
                                          input('...')
                                          print('tra il carbone ormai bruciato trovi una chiave di bronzo!')
                                          chiave = 1  #prendi la chiave e esci dal ciclo for
                                          break
                                      else:
                                          print('ti avvicini ma non trovi niente')
                                          print('(hai ', 4-j ,' tentativi)')


                                else:
                                    if j ==4 :
                                        break
                                    if chiave == 1:
                                        break #esci dal secondo for
                                    print('no mi dispiace')
                                    print('(hai ', 4-i ,' tentativi)')
                                if chiave==1:
                                    break


                        print('a questo punto esci dalla stanza')
                        input('...')
                        s9= input('provi ad aprire l\'altra porta o vai verso le scale?')
                        if s9.find ('ort')>0 or s9.find('pr')>0:
                            input('...')
                            if chiave == 1:
                                print('la chiave gira nella serratura...')
                                input('...')
                                print('decidi di entrare')
                                input('...')
                                print('la stanza ha le finestre oscurate, come le altre due, pero\' non ci sono lampadine')
                                print('l\'unico flebile bagliore viene da due candele poste ai lati di un letto')
                                input('...')
                                print('ti avvicini al letto, e\' vuoto, ma non e\' un letto normale')
                                print('sembra piu\' un letto da ospedale; in un angolo della stanza c\'e\' addirittura una grossa macchina per dialisi ')
                                s10= input('vuoi fare un giro della stanza o esci e richiudi a chiave?')
                                if s10.find('giro')>0 or s10.find('tanza'):
                                    print('prendi una delle candele e inizi a ispezionare la stanza...')
                                    input('...')
                                    print('alle pareti sono appesi dei disegni di bambino')
                                    print('uno in particolare rappresenta una bambina con un foglietto in mano')

                                    print('con accanto un uomo adulto con in mano dei fogli e una penna.')
                                    print('entrambi i personaggi hanno un sorriso che va da orecchio a orecchio')
                                    input('...')
                                    print('al margine di un\'altro disegno trovi una scritta, capisci subito che e\' di un adulto')
                                    input('...')
                                    print('                       \'Che bel giorno e\' stato! Veramente memorabile!')
                                    print('                        Se il dopodomani di ieri e\' pasqua allora questa bella giornata e\' l\'altro ieri di domani... \'')
                                    print('posi la candela ed esci dalla stanza')
                            #sei di nuovo fuori dalle stanze
                            if chiave == 0:
                                print('non hai la chiave...')
                        print('sei nel corridoio, ti avvicini alle scale')
                        s4=' scale'
                if s4.find ('cale')>0:
                    print('scendi le scale, questo posto deve essere una casa padronale o qualcosa del genere...')
                    print('lungo tutta la rampa di scale sono appesi dei ritratti, i soggetti passano velocemente')
                    print('da una bambina felice sui dodici anni ad una sorta di spettro pallido...')
                    input('...')
                    print('i lineamenti sono ancora gli stessi, ma non rimane nulla di quella gaiezza e spensieratezza dei')
                    print('ritratti precedenti. L\'ultimo ritratto della serie raffigura una giovane pallida, senza vita.')
                    print('a giudicare dalla data apposta alla firma tremante risale a solamente due anni fa\'.')
                    input('...')
                    print('sei arrivato alla fine delle scale, si apre davanti a te un ampio ingresso.')
                    print('alla tua destra e alla tua sinistra ci sono due porte di legno, in fondo invece c\'e\' una pesante porta blindata,')
                    print('alta almeno tre metri e larga due. Ai lati dell\'ingresso ci sono due grandi sale speculari non limitate da porte')
                    #sei nell'atrio
                    s11=input('cosa vuoi fare? provare ad aprire le porte di legno, entrare in una delle due sale o tentare di forzare la porta blindata?')
                    #provi ad entrare nelle porte di legno
                    if s11.find('rovo')>0 or s11.find('pr')>0 or s11.find('legno')>0:
                        print('sembrano essere entrambe chiuse a chiave')
                    #provi o la port blindata o le scale
                        s11=input('cosa vuoi fare? entrare in una delle due sale o tentare di forzare la pota blindata?')
                    if s11.find('orz')>0 or s11.find('blindata')>0 or s11.find('ent')>0:
                        print('non la sposti neanche di un millimetro...')
                        print('a questo punto non puoi fare altro che andare in una sala')
                        s11= 'asal'
                    #entri nella sala
                    if s11.find('ntr')>0 or s11.find('due')>0 or s11.find('sal')>0:
                        input('...')
                        print('Sei entrato nella sala di sinistra, ')
                        print('c\'e\' una grande tavolata che la percorre in tutta la sua lunghezza; le decorazioni sulle pareti sono ricche di intarsi in legno,')
                        print('deve essere la villa di un barone o lord, o comunque di un aristocratico facoltoso.')
                        print('fai un giro della sala...')
                        input('...')
                        print('in fondo alla sala, sul lato opposto della porta da cui sei entrato c\'e\' un enorme camino, con alla sommita\' degli stemmi nobiliari')
                        print('su una parete e\' appeso un dipinto, delle stesse dimensioni degli altri, ma non contiene nessun ritratto. ')
                        print('Sembra un dipinto astratto, ci sono soltanto scritte senza significato e schizzi rossi e neri.')
                        input('...')
                        print('controlli la data, e\' cronologicamente l\'ultimo trovato nella casa')
                        input('...')
                        #esci dalla stanza o cerchi la cassaorte?
                        s12= input('continui a cercare indizi o cambi sala?')
                        if s12.find('ontinu')>0 or s12.find('cerc')>0 or s12.find('indizi')>0:
                            print('ispezioni ogni angolo della grande sala, apri tutti i cassetti e i mobili da argenteria che ci sono in giro,')
                            print('quando ad un tratto scopri, dentro un basso armadietto una cassaforte...')
                            input('...')
                            print('sembra che sia chiusa, serve un codice di 4 cifre per poterla aprire...')
                            print(' c\'e\' anche un biglietto con scritto: \'il codice lo sai, ce l\'hai gia\' in mente...')
                            for h in range (0,3):
                                c1 = (input('prima cifra: '))
                                c2 = (input('seconda cifra: '))
                                c3 = (input('terza cifra: '))
                                c4 = (input('quarta cira: '))
                                if c1== '5' and c2== '8' and c3 == '9' and c4== '0':
                                    print('Si e\' aperta!!')
                                    lettera =1
                                    input('...')
                                    print('dentro c\'e\' soltanto una lettera')
                                    print(' ')
                                    print('                                          Ultime volonta\' di Evelin Riddle')
                                    print(' ')
                                    print('                      Caro marito, ti scrivo questa lettera in uno dei miei ultimi momenti di lucidita\'.')
                                    print('                      Il dolore che ho provato e che continua a dilaniarmi dentro non potra\' finire che')
                                    print('                      con il mio ricongiungimento con Molly. Non posso sopportare di vivere ancora in un ')
                                    print('                      mondo senza mia figlia. ')
                                    print('                      ma prima di fare questo fatidico gesto sento il bisogno di liberare la mia anima da')
                                    print('                      un peso che mi porto dentro da moltissimi anni.')
                                    print('                      Quando ancora non eravamo sposati io rimasi in cinta di te. Non essendo stato programmato')
                                    print('                      il nostro matrimoni temetti per il mio buon nome, percio\' feci quel ritiro spirituale  ')
                                    print('                      che mi separo\' il tempo necessario per dare alla luce nostro figlio.')
                                    print('                      Quello che accadde a qualla innocente creaturina lo ignoro. Lo affidai al convento nel quale')
                                    print('                      mi trovavo e non seppi piu\' nulla.')
                                    print('                      Con questa lettera ti consegno anche il compito di cercare piu\' informazioni possibili sul')
                                    print('                      destino di nostro figlio, se e\' stato adottato da una famiglia o se come la nostra Molly ')
                                    print('                      non e\' piu\' su questa terra. In tal caso tra poco lo riabbracero\'. \n')
                                    print('                      Evelin')
                                    break
                                else:
                                    print('non si apre...')
                            #se non aveva visto lo scpecchio...
                            if lettera != 1:
                                print('proprio non riesci ad aprlirla...')
                                input('...')
                                print('forse non hai trovato tutti gli indizi sparsi nella casa...')
                                print('continui a fare il giro della stanza')
                                input('...')
                                print(' ad un certo punto ti spaventi per il tuo riflesso su un anta di un mobile decorato con piccoli frammenti di vetro riflettente')
                                print(' ti avvicini a guardare meglio la tua immagine frammentata...')
                                input('...')
                                print('ti accorgi allora di avere una scritta sulla fronte!')
                                print(' c\'e\' scritto... ')
                                print('                                    5890')
                                input('cosa fai?')
                                print('riapri l\'armadietto, ti appressi a inserire il codice... ')
                                for k in range (0,5):
                                    c1 = (input('prima cifra: '))
                                    c2 = (input('seconda cifra: '))
                                    c3 = (input('terza cifra: '))
                                    c4 = (input('quarta cira: '))
                                    if c1== '5' and c2== '8' and c3 == '9' and c4== '0':
                                        print('Si e\' aperta finalmente!!')
                                        input('...')
                                        print('dentro c\'e\' soltanto una lettera:')
                                        print(' ')
                                        print('                                          Ultime volonta\' di Evelin Riddle')
                                        print(' ')
                                        print('                      Caro marito, ti scrivo questa lettera in uno dei miei ultimi momenti di lucidita\'.')
                                        print('                      Il dolore che ho provato e che continua a dilaniarmi dentro non potra\' finire che')
                                        print('                      con il mio ricongiungimento con Molly. Non posso sopportare di vivere ancora in un ')
                                        print('                      mondo senza mia figlia. ')
                                        print('                      ma prima di fare questo fatidico gesto sento il bisogno di liberare la mia anima da')
                                        print('                      un peso che mi porto dentro da moltissimi anni.')
                                        print('                      Quando ancora non eravamo sposati io rimasi in cinta di te. Non essendo stato programmato')
                                        print('                      il nostro matrimonio temetti per il mio buon nome, percio\' feci quel ritiro spirituale  ')
                                        print('                      che mi separo\' il tempo necessario per dare alla luce nostro figlio.')
                                        print('                      Quello che accadde a quella innocente creaturina lo ignoro. Lo affidai al convento nel quale')
                                        print('                      mi trovavo e non seppi piu\' nulla.')
                                        print('                      Con questa lettera ti consegno anche il compito di cercare piu\' informazioni possibili sul')
                                        print('                      destino di nostro figlio, se e\' stato adottato da una famiglia o se come la nostra Molly ')
                                        print('                      non e\' piu\' su questa terra. In tal caso tra poco lo riabbracero\'. \n')
                                        print('                      Evelin')
                                        lettera = 1
                                        break
                                    else:
                                        print('non si apre...')
                        if s12.find('amb') or s12.find('sala') or lettera ==1:
                            #adesso hai sicuramente la lettera
                            input('...')
                            print('esci dalla sala')
                            input('...')
                            print('ti chiedi perche\' ti stanno facendo questo, perche\' sei rinchiuso in questa casa.')
                            input('...')
                            print('entri nell\'altra sala')
                            input('...')
                            print('questa sala e\' grande quanto quella precedente, ma e\' stata adibita ad un\'altra funzione.')
                            print('sembra essere la sala dei ricevimenti, non ci sono mobili o tavolate al centro della stanza;')
                            print('probabilmente era usata anche per dare feste danzanti, come suggerisce il parquet. ')
                            print('Vicino al camino ci sono alcune grandi poltrone.')
                            input('...')
                            print('ti stai per sedere in una di queste quando ti accorgi che sopra ogni poltrona c\'e\' una busta con una scritta sopra...')
                            print('poltrona 1 : LUNEDI\'')
                            print('poltrona 2 : MARTEDI\'')
                            print('poltrona 3 : MERCOLEDI\'')
                            print('poltrona 4 : GIOVEDI\'')
                            print('poltrona 5 : VENERDI\'')
                            print('poltrona 6 : SABATO')
                            print('poltrona 7 : DOMENICA')
                            print('c\'e\' anche un biglietto appoggiato sopra il camino:')
                            print('                                    \'Un giorno in particolare e\' stato veramente memorabile,')
                            print('                                       solo una lettera conterra\' un\'informazione utile a trovare il prossimo indizio\'')
                            for m in range (0, 7):
                                s13 = int(input('quale numero apri?'))
                                #ogni possibilita di lettera
                                if s13==1 :
                                    print('sono fatta di legna ma non posso essere tagliata')
                                if s13==2 :
                                    print('costruisco ponti fatti d\'argento e corone fatte d\'oro')
                                if s13==3 :
                                    print('ho una testa ma sono priva di corpo')
                                if s13==4 :
                                    print('unisco due persone ma ne tocco una soltanto')
                                if s13==5 :
                                    print('senza testa sono piu\' alto, con la testa sono piu\' basso')
                                if s13==6 :
                                    print('sono bianca, sono rotonda, ma non sempre intorno. A volte mi vedi a volte no')
                                if s13==7 :
                                    print('piu\' grande di dio e piu\' cattivo del diavolo, i poveri lo hanno, i ricchi non ne hanno bisognoe se lo mangi morirai')
                                input('...')
                                s14 =input('ne apri un\'altra?')
                                if s14=='no':
                                    break
                            #devi salire in camera
                            for w in range(0,5):
                                if w == 2 :
                                    #suggerimento
                                    s21= input('vuoi un suggerimento?')
                                    if s21=='si':
                                        suggerimento= suggerimento-1
                                        print('e\' qualcosa che stava nella stanza in cui ti sei svegliato, ma la testa in questionenon e\' sua, ma tua...')

                                s15 = input('hai pensato dove vuoi andare adesso?')
                                if s15.find('uscin')>0 or s15.find('piano')>0 or s15.find('etto')>0 or s15.find('scale')>0 or s15.find('sco')>0 or s15.find('amer')>0 or s15.find('stanz')>0 or s15.find('algo')>0:
                                    print('esci dalla sala, sei nell\'atrio')
                                    input('...')
                                    print('sali le scale ')
                                    input('...')
                                    print('entri nella stanza i cui ti sei svegliato')
                                    print('ti avvicinialla brandina e alzi il cuscino...')
                                    print('c\'e\' una chiave dorata!')
                                    chiave = 2
                                    input('...')
                                    break
                                else:
                                    print('non trovi niente...')
                                    print('(hai ', 4-w ,' tentativi)')
                            print('ti precipiti giu\' per le scale, senti di avvicinarti ogni passo di piu\' alla soluzione')
                            s16 = input('cosa fai una volta arrivato nell\'atrio? ci sono ancora le due porte di legno chiuse e quella di ingresso blindata')
                            #prova la porta blindata
                            if s16.find('gresso')>0 or s16.find('lindata')>0 or s16.find('scire')>0 or s16.find('sco')>0:
                                print('la chiave e\' troppo piccola, non entra nella serratura')
                                s16 = input('dove vai?')
                            if s16.find('egno')>0:
                               if chiave ==2:
                                print('ti avvicine alla porta di legno di sinistra, provi ad aprire ma la chiave non gira...')
                                input('...')
                                print('non rimane che provare la porta di destra...')
                                print('si apre, entri dentro')
                                input('...')
                                print('sembra una stanza dei giochi')
                                print('c\'e\' un lettino a culla, una potrona a dondolo e tanti scaffali e cassapanche pieni di balocchi impolverati')
                                input('...')
                                print('questa doveva essere la stanza di Molly prima che si ammalasse...')
                                print('deve aver avuto una bella infanzia dopotutto, tutti questi giochi tu non potevi neanche immaginarli')
                                input('...')
                                print(' ti fai un giro della stanza')
                                input('...')
                                print('ci sono altri disegni della bambina su di un tavolino... ha fatto il ritratto della madre mentre dipinge.')
                                print('Ce n\'e\' anche uno del padre intento a  nascondere un orsacchiotto dietro ad una poltrona mentre lei si copre gli occhi con le manine.')
                                input('...')
                                print(' in mezzo ai tutti quei giochi ce n\'e\' uno che attira la tua attenzione. E\' l\'unico a non essere impolverato ')
                                print(' lo prendi in mano per esaminarlo...')
                                print(' sembra essere un contenitore di legno, ha una forma cilindrica, della grandezza di una bottiglia.')
                                print(' dentro c\'e\' qualcosa di metallico...')
                                input('...')
                                print('ti accorgi che ci sono dei cilindri rotanti lungo la superficie laterale del contenitore')
                                print('ogni cilindretto e\' formato dalle lettere dell\'alfabeto')
                                print('per apriro bisogna disporre i cilindretti per formare una parola... di 6 lettere')
                                print('sul lato del cilindro e\' invece inciso \'\'E\' IMPOSSIBILE\'\' ')
                                s17=input('cosa scrivi ruotando i cilindri? ')
                                for q in range (0,5):
                                    if s17.find ('IENTE')>0 or s17.find ('iente')>0 or s17 =='niente':
                                        print('senti un click')
                                        input('...')
                                        print('giri il coperchio che ti rimane in mano')
                                        print('dentro ci sono 2 chiavi! una dorata e una di ferro')
                                        chiave = 3
                                        input('...')
                                        print('su quella di ferro c\'e\'una targhetta con scritto \'\'uscita\'\'')
                                        break

                                    else:
                                        print('il contenitore resta chiuso...')
                                        #suggerimento
                                        if q== 2:
                                            s22= input('vuoi un suggerimento?')
                                            if s22=='si':
                                                print('p.s. ')
                                                suggerimento= suggerimento-1
                                            if s22== 'si' and suggerimento== 0:
                                                print('hai finito i suggerimenti...')
                                        print('(hai ', 4-q ,' tentativi)')
                                        s17= input('prova ancora')

                                input('...')
                                print('esci dalla stanza dei giochi')
                                if chiave == 3:
                                    s18 = input('cosa fai? usi la chiave dorata per aprire l\'ultima porta di legno o esci dalla porta d\'ingresso?')
                                if s18.find('egno')>0 or s18.find('dorata')>0 or s18.find('ultima')>0:
                                    print('ti avvicini lentamente all\'ultima porta...')
                                    input('...')
                                    print('inserisci la chiave nella serratura e giri')
                                    input('...')
                                    print('apri la porta. Sei impietrito. ')
                                    print('ti trovi davanti ad un letto a baldacchino, ma nel letto giace una persona')
                                    input('...')
                                    print('e\' un vecchio signore, con i capelli quasi tutti canuti e uno sguardo penetrante')
                                    print('I suoi lineamenti sono nobili, vedi qualcosa di familare nel suo volto.')
                                    input('...')
                                    print('--- Avvicinati --- ti sussurra ')
                                    print('ti metti al suo capezzale, senza dire una parola')
                                    input('...')
                                    print('--- Come immagino avrai capito io sono tuo padre...---')
                                    input('...')
                                    print('questa rivelazione ti scovolge, anche se intimamente ci speravi, non eri riuscito a formulare questo pensiero coscientemente.')
                                    print('ti senti stordito dalle sue parole, e rimani in silenzio')
                                    input('...')
                                    print('--- se avessi saputo prima di avere un figlio ti avrei cercato fino in capo al mondo, lo giuro. Ma come avrai letto sono venuto a ')
                                    print('conoscienza della tua esistenza solo dopo il tragico suicidio di Evelin, mia moglie... e tua madre.')
                                    print('Una volta ritrovato ho deciso di sottoporti a questo percorso ad enigmi per metterti alla prova, dopo tutto se sei mio figlio ')
                                    print('non avrai trovato molte difficolta\' e il solo fatto che sei qui dentro, al mio cospetto, ne e\' la prova.')
                                    print('devi sapere che questi percorsi erano il gioco preferito di mia figlia, Molly, la sorellina che non hai mai conosciuto.---')
                                    input('...')
                                    print('ormai hai le lacrime agli occhi, tutte le risposte che cercavi da una vita, dalla tua vita, ti vengono rivelate velocemente ')
                                    print('e chiaramente da quell\'anziano signore che provi ad immaginare come \'padre\'')
                                    input('...')
                                    print('--- mio caro ragazzo, su quella scrivania ci sono i documenti del mio testamento, ti ho reso l\'unico beneficiario della mia eredita\'.')
                                    print('ma adesso mettiti comodo, non ho intenzione di lasciare questo mondo per ancora un po\'---')
                                    print('disse con un sorriso tenero e con gli occhi gia\' lucidi')
                                    print('--- e io e te abbiamo tantissime cose di cui parlare ---')
                                    input('...')
                                    s19 = input('lo abbracci o esci dalla stanza ?')
                                    if s19.find ('sco')>0 or s19.find ('tanza')>0:
                                        print('per un momento ci avevi quasi creduto')
                                        print('ma chi si crede di essere quest\'uomo?! Non puoi rapire uno e rinchiuderlo in una casa per divertimento')
                                        print('come se tu ci potessi credere di essere suo figlio poi...')
                                        print('vabbe, per fortuna hai la chive per uscire. ')
                                        print('meglio alzare i tacchi prima che ci ripensi!')

                                    if s19.find ('bbraccio')>0:
                                        print('solo allora ti protendi verso quel docile vecchietto e lo abbracci affetuosamente, e per la prima volta ti senti a Casa.')

                                input('...')

                                if s18.find('sco')>0 or s18.find('ngresso')>0 or s18.find('lindata')>0:
                                    print('ti avvicini alla pesante porta di ingresso, usi la chiave di ferro per aprirla... ')
                                    input('...')
                                    print('funziona! sei finalmente libero!')
                                    input('...')
                                    print('il portone si chiude bruscamente dopo il tuo passaggio')
                                    print('ti allontani di qualche passo dalla magione e ti rendi conto della sua notevole grandezza')
                                    print('inizi a correre verso il cancello del giardino, finche non lo superi e rimani in mezzo ad una strada di campagna')
                                    input('...')
                                    print('hai ancora molte domande pero\' che vogliono una risposta...')
                                    print('ma questa risposta non potrai scoprirla se non vivendo...')
                                    input('...')
                                    print('adesso potrai continuare con la tua vita di sempre; pero\' ogni sera, prima di addormentarti nel tuo povero')
                                    print('letto del tuo monolocale penserai a quella avventura, e  a quello che sarebbe successo se avessi aperto l\'Ultima porta...')
                                    input('...')
                                fine = 1
                                print(' ')
                                print(' ')
                                print('                                                     FINE')
                                input('...')
                                print(' \n \n \n ')
                                print('Credits ')
                                print('---------------Story    Stefano & Roberto La Commare')
                                print('---------------Code     Roberto La Commare')

if fine !=1:
    print(' ')
    print(' ')
    print('GAME OVER')







