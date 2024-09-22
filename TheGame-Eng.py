#!/usr/bin/env python3

#DO YOU WANT TO PLAY?

start = input('do you want to play? ')
letter = 0
hint = 3
key = 0
end = 0
j = 0
if start == 'yes' or start == ' yes':
    #rules
    print('                                         RULES OF THE GAME')
    print('               after a question respond by writing \'yes\' or \'no\' if requested and press ENTER')
    print('               otherwise type the alternative you choose as completely as possible and press ENTER')
    print('               if \n               ...\n               appears press ENTER')
    print('               you can use 3 hints if necessary, you have 5 attempts for each puzzle')
    print('               have fun!')
    input('...')
    #INTRODUCTION
    print('You are a 32-year-old man. Your story began in a nuns\' boarding school,')
    print('being an orphan you\'ve always had to face life alone,')
    print('and up to now, your existence hasn\'t led you anywhere...')
    input('...')
    print('but where are you now? you are lying on a cot, there\'s a small light brightening the room')
    print('you try to think of the last thing you remember... you were walking when you felt an insect bite on your neck')
    print('and then nothing more. They must have drugged you, you still feel a slight headache')
    input('...')
    print('you need to think about what your next move will be')
    #first choice
    s1 = input('do you start shouting hoping someone will hear you or get up and inspect the room?')
    if s1.find('shout') > 0 or s1.find('rl') > 0:
        print('it doesn\'t seem to have solved anything...')
        s1 = input('and now? ')
    if s1.find('oom') > 0 or s1.find('spect') > 0 or s1.find('et up') > 0 :
        print('in the room you find a desk with a letter on it, a mirror, and obviously a door')
        #second choice
        s2 = input('where do you go? ')
        #if you look in the mirror
        if s2.find('rror') > 0:
            print('you look in the mirror, you immediately notice there is a writing on your forehead,')
            print('\'5890\'')
            print('luckily it\'s a marker, with a bit of rubbing you manage to erase it')
            #decide either door or letter
            s2 = input('where do you go now? ')
        if s2.find('esk') > 0 or s1.find('etter') > 0:
            print('you read the letter...')
            input('...')
            print('             Beloved Molly,')
            print('             you kept asking me what the gift I was carefully preparing for your eleventh birthday was.')
            print('             It\'s finally time for you to know.')
            print('             I have created the most difficult and complex puzzle path I have ever made for you.')
            print('             the games I made for you when you were younger are nothing compared to this.')
            print('             I hope you like it, happy birthday darling!')
            print('             your old father \n')
            print('             p.s. never forget that nothing is impossible')
            input('...')
            s2 = input('now do you go to the mirror or exit through the door? ')
            if s2.find('rror') > 0:
                print('you look in the mirror, you immediately notice there is a writing on your forehead,')
                print('\'5890\'')
                print('luckily it\'s a marker, with a bit of rubbing you manage to erase it')
                s2 = ' door'
            #go to the door
        if s2.find('oor') > 0 or s2.find('xit') > 0:
            print('now you open the door, it seems to lead to a dark corridor...')
            #choose if you turn on the light
            s3 = input('do you try to turn on the light? ')
            if s3 == 'no':
                print('okay, too bad you\'re not a cat with night vision... better turn on the light!')
                s3 = 'yes'
            if s3 == 'yes' or s3 == ' yes':
                print('okay, now you can see that the corridor opens onto two doors and a staircase leading down to the lower floor... \nit must not be a small building')
                input('...')
                # do you try the doors or go down the stairs?
                s4 = input('do you try to open the doors or go down the stairs? ')
                if s4.find('oor') > 0:
                    print('one door is locked, while the other is open')
                    #what do you do do you enter or not?
                    s5 = input('do you enter?')
                    if s5 == 'yes' or s5 == ' yes':
                        print('you\'re inside, you look around, you only see a small wardrobe, a chair in front of an unlit fireplace,')
                        print('an artist\'s easel with a stool nearby and assorted oil paints and brushes')
                        #do you exit rummage or sit?
                        s6 = input('do you exit, rummage around the room looking for clues \nor do you sit on the chair for a moment to reflect? ')
                        if s6.find('hair') > 0 or s6.find('eflect') > 0 or s6.find('it') > 0:
                            print('you are very comfortable in this chair...')
                            input('...')
                            input('...')
                            input('...')
                            input('...')
                            print('you were almost falling back asleep when your attention was caught by the numerous portraits hanging on the walls')
                            input('...')
                            print('you get up from the chair and approach the paintings...')
                            input('...')
                            print('you notice they are all of the same subject')
                            print('it\'s probably the girl from the letter...')
                            print('there is a portrait for every year, they must have been made by someone who loved her very much')
                            input('...')
                            print('next to the date at the bottom left there is also the signature \'Evelin\'')
                            print('maybe it\'s the mother...')
                            s6 = input('do you exit or rummage around the room?')
                        if s6.find('mmage') > 0:
                            print('everything seems so dusty, this room must not have been opened for a long time...')
                            print('in the wardrobe there are only old rags and more oil paints')
                            print('wait a moment, what\'s this?')
                            input('...')
                            print('there is a small piece of paper among the brushes, there are a few lines written in pen...')
                            print('        I am she who enters first and then opens, you need me')
                            print('        I am in the middle of that which, when bought, is black, when used is red and when it becomes useless is white')
                            input('...')
                            #solve the riddle first part
                            for i in range(0, 5):
                                #hint
                                if i == 2:
                                    s20 = input('do you want a hint?')
                                    if s20 == 'yes':
                                        hint -= 1
                                        print('it\'s used to open doors...')
                                s7 = input('what should you look for? ')

                                if s7.find('ey') > 0:
                                    print('we\'re getting there!')
                                    #solve the riddle second part
                                    for j in range(0, 5):

                                        if j == 2:
                                            s20 = input('do you want a hint?')
                                            if s20 == 'yes':
                                                hint -= 1
                                                print('it\'s something present in the room...')
                                        s8 = input('Where should you look for it? ')
                                        if s8.find('replace') > 0 or s8.find('ire') > 0 or s8.find('shes') > 0 or s8.find('arcoal') > 0:
                                            print('you approach the fireplace, start to stir the ashes... ')
                                            input('...')
                                            print('among the burnt charcoal you find a bronze key!')
                                            key = 1  # take the key and exit the for loop
                                            break
                                        else:
                                            print('you approach but find nothing')
                                            print('(you have ', 4-j, ' attempts)')


                                else:
                                    if j == 4:
                                        break
                                    if key == 1:
                                        break  # exit the second for loop
                                    print('no, sorry')
                                    print('(you have ', 4-i, ' attempts)')
                                if key == 1:
                                    break


                        print('at this point you exit the room')
                        input('...')
                        s9 = input('do you try to open the other door or head to the stairs?')
                        if s9.find('oor') > 0 or s9.find('pen') > 0:
                            input('...')
                            if key == 1:
                                print('the key turns in the lock...')
                                input('...')
                                print('you decide to enter')
                                input('...')
                                print('the room has shaded windows like the other two, but there are no light bulbs')
                                print('the only faint glow comes from two candles placed on either side of a bed')
                                input('...')
                                print('you approach the bed, it\'s empty, but it\'s not a regular bed')
                                print('it looks more like a hospital bed; in a corner of the room there is even a large dialysis machine')
                                s10 = input('do you want to inspect the room or exit and lock the door again?')
                                if s10.find('spect') > 0 or s10.find('oom'):
                                    print('you take one of the candles and start to inspect the room...')
                                    input('...')
                                    print('the walls are lined with children\'s drawings')
                                    print('one in particular depicts a girl with a piece of paper in her hand')

                                    print('next to a grown man holding some papers and a pen.')
                                    print('both characters have ear-to-ear smiles')
                                    input('...')
                                    print('at the margin of another drawing you find a writing, you immediately understand it\'s from an adult')
                                    input('...')
                                    print('                       \'What a beautiful day it was! Truly remarkable!')
                                    print('                        If the day after tomorrow is Easter then that wonderful day is the day before yesterday of tomorrow... \'')
                                    print('you place the candle down and exit the room')
                            #you are again outside the rooms
                            if key == 0:
                                print('you don\'t have the key...')
                        print('you are in the corridor, you approach the stairs')
                        s4 = ' stairs'
                if s4.find('airs') > 0:
                    print('you go down the stairs, this place must be a manor house or something like that...')
                    print('along the entire staircase, portraits are hung, the subjects quickly change')
                    print('from a happy girl about twelve years old to a sort of pale specter...')
                    input('...')
                    print('the features are still the same, but there is nothing left of that cheerfulness and carefree nature')
                    print('of the previous portraits. The last portrait in the series depicts a young pale girl, lifeless.')
                    print('judging by the date next to the shaky signature, it was made only two years ago.')
                    input('...')
                    print('you have reached the bottom of the stairs, a large hall opens before you.')
                    print('to your right and left there are two wooden doors, while in the back there is a heavy armored door,')
                    print('at least three meters high and two meters wide. On either side of the hall there are two large, symmetrical rooms not enclosed by doors')
                    #you are in the atrium
                    s11 = input('what do you want to do? try to open the wooden doors, enter one of the two rooms or try to force the armored door?')
                    #you try to enter the wooden doors
                    if s11.find('ry') > 0 or s11.find('pen') > 0 or s11.find('ood') > 0:
                        print('they both seem to be locked with a key')
                    #try either the armored door or the stairs
                        s11 = input('what do you want to do? enter one of the two rooms or try to force the armored door?')
                    if s11.find('orce') > 0 or s11.find('rmored') > 0 or s11.find('nter') > 0:
                        print('you don\'t move it even an inch...')
                        print('at this point, you have no choice but to enter a room')
                        s11 = 'rooms'
                    #enter the room
                    if s11.find('nter') > 0 or s11.find('wo') > 0 or s11.find('ooms') > 0:
                        input('...')
                        print('You have entered the left room,')
                        print('there\'s a big table running the entire length of the room; the wall decorations are richly carved in wood,')
                        print('this must be the villa of a baron or lord, or anyway of a wealthy aristocrat.')
                        print('you take a tour around the room...')
                        input('...')
                        print('at the end of the room, opposite the door you entered through, there is a huge fireplace, with noble crests at the top')
                        print('on one wall, there is a painting, same dimensions as the others, but it doesn\'t contain any portraits.')
                        print('It looks like an abstract painting, there are only meaningless writings and red and black splashes.')
                        input('...')
                        print('you check the date, it\'s the last one chronologically found in the house')
                        input('...')
                        #do you exit the room or look for the safe?
                        s12 = input('do you continue looking for clues or change room?')
                        if s12.find('ntinue') > 0 or s12.find('ook') > 0 or s12.find('lues') > 0:
                            print('you inspect every corner of the large room, open all the drawers and silverware cabinets around,')
                            print('when suddenly you discover, inside a low cabinet a safe...')
                            input('...')
                            print('it seems to be closed, you need a 4-digit code to open it...')
                            print(' there is also a note that says: \'you know the code, you already have it in mind...')
                            for h in range(0, 3):
                                c1 = (input('first digit: '))
                                c2 = (input('second digit: '))
                                c3 = (input('third digit: '))
                                c4 = (input('fourth digit: '))
                                if c1 == '5' and c2 == '8' and c3 == '9' and c4 == '0':
                                    print('It\'s opened!!')
                                    letter = 1
                                    input('...')
                                    print('inside there is just one letter')
                                    print(' ')
                                    print('                                          Last will of Evelin Riddle')
                                    print('                                          Last will of Evelin Riddle')
                                    print(' ')
                                    print('                      Dear husband, I write you this letter in one of my last moments of lucidity.')
                                    print('                      The pain I have felt and that continues to tear me apart can only end')
                                    print('                      with my reunion with Molly. I cannot bear to live in a world without my daughter.')
                                    print('                      but before making this fateful gesture I feel the need to free my soul from')
                                    print('                      a burden I have carried inside for many years.')
                                    print('                      When we were not yet married I got pregnant by you. Since our marriage was not planned')
                                    print('                      I feared for my good name, so I took that spiritual retreat')
                                    print('                      that separated me for the necessary time to give birth to our son.')
                                    print('                      What happened to that innocent little creature I do not know. I entrusted it to the convent where')
                                    print('                      I stayed and I never knew anything else.')
                                    print('                      With this letter I also hand you the task of finding as much information as possible about')
                                    print('                      our son\'s fate, if he was adopted by a family or if like our Molly ')
                                    print('                      he is no longer on this earth. In such case soon I will hold him again.\n')
                                    print('                      Evelin')
                                    break
                                else:
                                    print('it does not open...')
                                    #if he hadn't seen the mirror...
                            if letter != 1:
                                print('you just can\'t open it...')
                                input('...')
                                print('maybe you haven\'t found all the clues scattered around the house...')
                                print('you continue to explore the room')
                                input('...')
                                print(' you get scared by your reflection on a door of a piece of furniture decorated with small reflective glass fragments')
                                print(' you approach to look better at your fragmented image...')
                                input('...')
                                print('you then realize you have a writing on your forehead!')
                                print(' it says...')
                                print('                                    5890')
                                input('what do you do?')
                                print('you open the cabinet again, you get ready to enter the code...')
                                for k in range(0, 5):
                                    c1 = (input('first digit: '))
                                    c2 = (input('second digit: '))
                                    c3 = (input('third digit: '))
                                    c4 = (input('fourth digit: '))
                                    if c1 == '5' and c2 == '8' and c3 == '9' and c4 == '0':
                                        print('It\'s finally opened!!')
                                        input('...')
                                        print('inside there is just one letter:')
                                        print(' ')
                                        print('                                          Last will of Evelin Riddle')
                                        print(' ')
                                        print('                      Dear husband, I write you this letter in one of my last moments of lucidity.')
                                        print('                      The pain I have felt and that continues to tear me apart can only end')
                                        print('                      with my reunion with Molly. I cannot bear to live in a world without my daughter.')
                                        print('                      but before making this fateful gesture I feel the need to free my soul from')
                                        print('                      a burden I have carried inside for many years.')
                                        print('                      When we were not yet married I got pregnant by you. Since our marriage was not planned')
                                        print('                      I feared for my good name, so I took that spiritual retreat')
                                        print('                      that separated me for the necessary time to give birth to our son.')
                                        print('                      What happened to that innocent little creature I do not know. I entrusted it to the convent where')
                                        print('                      I stayed and I never knew anything else.')
                                        print('                      With this letter I also hand you the task of finding as much information as possible about')
                                        print('                      our son\'s fate, if he was adopted by a family or if like our Molly ')
                                        print('                      he is no longer on this earth. In such case soon I will hold him again.\n')
                                        print('                      Evelin')
                                        letter = 1
                                        break
                                    else:
                                        print('it does not open...')
                            if s12.find('oom') or s12.find('ange') or letter ==1:
                                #now you definitely have the letter
                                input('...')
                                print('you exit the room')
                                input('...')
                                print('you wonder why they are doing this to you, why you are locked in this house.')
                                input('...')
                                print('you enter the other room')
                                input('...')
                                print('this room is as big as the previous one, but it was used for another purpose.')
                                print('it seems to be the reception room, there are no furniture or tables in the center of the room;')
                                print('it was probably also used for dancing parties, as suggested by the parquet.')
                                print('Near the fireplace there are some large armchairs.')
                                input('...')
                                print('you are about to sit in one of these when you notice that there is an envelope above each armchair with a writing on it...')
                                print('armchair 1: MONDAY')
                                print('armchair 2: TUESDAY')
                                print('armchair 3: WEDNESDAY')
                                print('armchair 4: THURSDAY')
                                print('armchair 5: FRIDAY')
                                print('armchair 6: SATURDAY')
                                print('armchair 7: SUNDAY')
                                print('there is also a note placed on the fireplace:')
                                print('                                    \'One particular day was truly memorable,')
                                print('                                       only one letter will contain useful information to find the next clue\'')
                                for m in range(0, 7):
                                    s13 = int(input('which number do you open?'))
                                    #each letter possibility
                                    if s13 == 1:
                                        print('I am made of wood but cannot be cut')
                                    if s13 == 2:
                                        print('I build bridges made of silver and crowns made of gold')
                                    if s13 == 3:
                                        print('I have a head but am bodyless')
                                    if s13 == 4:
                                        print('I unite two people but only touch one')
                                    if s13 == 5:
                                        print('without a head I am taller, with a head I am shorter')
                                    if s13 == 6:
                                        print('I am white, I am round, but not always around. Sometimes you see me, sometimes not')
                                    if s13 == 7:
                                        print('greater than god and worse than the devil, the poor have it, the rich don\'t need it and if you eat it you will die')
                                    input('...')
                                    s14 = input('do you open another one?')
                                    if s14 == 'no':
                                        break
                                #you need to go upstairs
                                for w in range(0, 5):
                                    if w == 2:
                                        #hint
                                        s21 = input('do you want a hint?')
                                        if s21 == 'yes':
                                            hint -= 1
                                            print('it\'s something that was in the room where you woke up, but the head in question is not its, but yours...')

                                    s15 = input('have you thought about where you want to go now?')
                                    if s15.find('et out') > 0 or s15.find('loor') > 0 or s15.find('ed') > 0 or s15.find('tairs') > 0 or s15.find('xit') > 0 or s15.find('room') > 0 or s15.find('room') > 0 or s15.find('something') > 0:
                                        print('you leave the room, you are in the hall')
                                        input('...')
                                        print('you go upstairs ')
                                        input('...')
                                        print('you enter the room where you woke up')
                                        print('you approach the cot and lift the pillow...')
                                        print('there is a golden key!')
                                        key = 2
                                        input('...')
                                        break
                                    else:
                                        print('you don\'t find anything...')
                                        print('(you have ', 4-w, ' attempts)')
                                print('you rush downstairs, you feel yourself getting closer to the solution with every step')
                                s16 = input('what do you do once you reach the hall? there are still the two locked wooden doors and the armored entrance door')
                                #try the armored door
                                if s16.find('trance') > 0 or s16.find('rmored') > 0 or s16.find('xit') > 0 or s16.find('exit') > 0:
                                    print('the key is too small, it does not fit the lock')
                                    s16 = input('where do you go?')
                                if s16.find('ood') > 0:
                                  if key == 2:
                                    print('you approach the left wooden door, try to open it but the key does not turn...')
                                    input('...')
                                    print('there is nothing left but to try the right door...')
                                    print('it opens, you enter')
                                    input('...')
                                    print('it looks like a playroom')
                                    print('there is a cradle, a rocking chair and many shelves and toy chests full of dusty toys')
                                    input('...')
                                    print('this must have been Molly\'s room before she got sick...')
                                    print('she must have had a good childhood after all, all these toys you couldn\'t even imagine')
                                    input('...')
                                    print(' you take a tour of the room')
                                    input('...')
                                    print('there are more drawings by the child on a little table... she made a portrait of her mother while painting.')
                                    print('There is also one of the father hiding a teddy bear behind a chair while she covers her eyes with her little hands.')
                                    input('...')
                                    print(' among all those toys one catches your attention. It\'s the only one not covered in dust ')
                                    print(' you take it in your hands to examine it...')
                                    print(' it looks like a wooden container, cylindrical in shape, about the size of a bottle.')
                                    print(' inside there\'s something metallic...')
                                    input('...')
                                    print('you notice that there are rotating cylinders along the side surface of the container')
                                    print('each cylinder is made up of letters of the alphabet')
                                    print('to open it you need to arrange the cylinders to form a word... 6 letters long')
                                    print('on the side of the cylinder is inscribed \'\'NOTHING\'\' ')
                                    s17 = input('what do you write by rotating the cylinders? ')
                                    for q in range(0, 5):
                                        if s17.find('HING') > 0 or s17.find('hing') > 0 or s17 == 'nothing':
                                            print('you hear a click')
                                            input('...')
                                            print('you turn the lid which remains in your hand')
                                            print('inside there are 2 keys! one gold and one iron')
                                            key = 3
                                            input('...')
                                            print('on the iron one there\'s a tag that says \'\'exit\'\'')
                                            break
                                        else:
                                            print('the container remains closed...')
                                            #hint
                                            if q == 2:
                                                s22 = input('do you want a hint?')
                                                if s22 == 'yes':
                                                    hint -= 1
                                                    print('p.s. ')
                                                if s22 == 'yes' and hint == 0:
                                                    print('you\'ve used all your hints...')
                                            print('(you have ', 4-q, ' attempts)')
                                            s17 = input('try again')

                                    input('...')
                                    print('you exit the playroom')
                                    if key == 3:
                                        s18 = input('what do you do? use the gold key to open the last wooden door or exit through the main door?')
                                    if s18.find('ood') > 0 or s18.find('old') > 0 or s18.find('ast') > 0:
                                        print('you slowly approach the last door...')
                                        input('...')
                                        print('insert the key into the lock and turn it')
                                        input('...')
                                        print('open the door. You are petrified. ')
                                        print('you are in front of a canopy bed, but there is a person lying in the bed')
                                        input('...')
                                        print('it\'s an old man, with almost completely white hair and a penetrating gaze')
                                        print('His features are noble, you see something familiar in his face.')
                                        input('...')
                                        print('--- Come closer --- he whispers ')
                                        print('you sit at his bedside without saying a word')
                                        input('...')
                                        print('--- As you might have guessed I am your father...---')
                                        input('...')
                                        print('this revelation shocks you, although you secretly hoped for it, you weren\'t able to form this thought consciously.')
                                        print('you feel stunned by his words, and remain silent')
                                        input('...')
                                        print('--- if I had known I had a son I would have looked for you to the ends of the earth, I swear. But as you may have read I came to')
                                        print('know of your existence only after the tragic suicide of Evelin, my wife... and your mother.')
                                        print('Once found I decided to subject you to this puzzle path to test you, after all if you are my son ')
                                        print('you wouldn\'t have found many difficulties and the mere fact that you are in here, at my presence, is proof of that.')
                                        print('you should know that these paths were my daughter\'s favorite game, Molly, the little sister you never met.---')
                                        input('...')
                                        print('now you have tears in your eyes, all the answers you were looking for in your life, from your life, are revealed to you quickly ')
                                        print('and clearly by that elderly gentleman you try to imagine as \'father\'')
                                        input('...')
                                        print('--- my dear boy, on that desk there are my testament documents, I have made you the sole heir to my estate.')
                                        print('but now make yourself comfortable, I don\'t intend to leave this world for a while longer---')
                                        print('he said with a tender smile and already tearful eyes')
                                        print('--- and you and I have many things to talk about ---')
                                        input('...')
                                        s19 = input('do you hug him or leave the room?')
                                        if s19.find('xit') > 0 or s19.find('oom') > 0:
                                            print('for a moment you almost believed it')
                                            print('but who does this man think he is?! You can\'t just kidnap someone and lock them in a house for fun')
                                            print('as if you could believe you are his son then...')
                                            print('okay, luckily you have the key to get out. ')
                                            print('better to get out of here before he changes his mind!')

                                        if s19.find('hug') > 0:
                                            print('only then do you reach out to that gentle old man and hug him affectionately, and for the first time you feel at Home.')

                                    input('...')

                                    if s18.find('xit') > 0 or s18.find('oor') > 0 or s18.find('mored') > 0:
                                        print('you approach the heavy entrance door, use the iron key to open it... ')
                                        input('...')
                                        print('it works! you are finally free!')
                                        input('...')
                                        print('the door closes abruptly after you pass through it')
                                        print('you walk a few steps away from the mansion and realize its significant size')
                                        print('you start running towards the garden gate, until you pass it and remain in the middle of a country road')
                                        input('...')
                                        print('you still have many questions though that need answers...')
                                        print('but these answers can only be discovered by living...')
                                        input('...')
                                        print('now you can continue with your usual life; though every night, before falling asleep in your poor')
                                        print('bed in your studio, you will think about that adventure and what would have happened if you had opened the Last door...')
                                        input('...')
                                    end = 1
                                    print(' ')
                                    print(' ')
                                    print('                                                     END')
                                    input('...')
                                    print(' \n \n \n ')
                                    print('Credits ')
                                    print('---------------Story    Stefano & Roberto La Commare')
                                    print('---------------Code     Roberto La Commare')

if end != 1:
    print(' ')
    print(' ')
    print('GAME OVER')
