import os, random, math

outindex = "flash-out.html"
breaker = "<wbr>"
breakerFrequency = 4 # lower number = more common
alist = '''                                <a class="glink" href="#">%s</a>'''

# Make flash lists
# Just a premade list for now
flash_1 = ['1on1soccer.swf', '3dtanks.swf', 'abobosbigadventure.swf', 'achievementunlocked.swf', 'achievementunlocked2.swf', 'achievementunlocked3.swf', 'actionturnip.swf', 'adaran.swf', 'adrenaline.swf', 'americanracing1.swf', 'americanracing2.swf', 'arkandianrevenant.swf', 'armyofages.swf', 'awesomecars.swf', 'awesomeplanes.swf', 'battlepanic.swf', 'bloonsplayerpack2.swf', 'bloonsplayerpack3.swf', 'bloonsplayerpack4.swf', 'bloonsplayerpack5.swf', 'bloonstd1.swf', 'bloonstd3.swf', 'bloonstd4.swf', 'bloonstd5.swf', 'bobtherobber.swf', 'boombot2.swf', 'boxhead2play.swf', 'bubbletanks2.swf', 'bulletbill.swf', 'bullettimefighting.swf', 'burritobison.swf', 'burritobisonrevenge.swf', 'cactusmccoy.swf', 'cactusmccoy2.swf', 'cannonbasketball2.swf', 'cargobridge.swf', 'causality.swf', 'chibiknight.swf', 'clickerheroes.swf', 'computerbashing.swf', 'crushthecastle.swf', 'crushthecastle2.swf', 'cubefield.swf', 'cyclomaniacs2.swf', 'diggy.swf', 'donkeykong.swf', 'dontshootthepuppy.swf', 'doodledefender.swf', 'doom.swf', 'dragracing.swf', 'ducklife.swf', 'ducklife2.swf', 'ducklife3.swf', 'ducklife4.swf', 'earntodie.swf', 'earntodie2.swf', 'earntodiesuperwheel.swf', 'electricman2.swf', 'elephantquest.swf', 'epicbattlefantasy3.swf', 'epiccomboredux.swf', 'exitpath.swf', 'factoryballs.swf', 'factoryballs2.swf', 'factoryballs3.swf', 'factoryballs4.swf', 'fancypantsadventure.swf', 'fancypantsadventure2.swf', 'fancypantsadventure3.swf', 'flashflightsimulator.swf', 'flight.swf', 'fracuum.swf', 'freerider2.swf', 'getontop.swf', 'giveuprobot.swf', 'giveuprobot2.swf', 'hanger.swf', 'hanger2.swf', 'happywheels.swf', 'hobo.swf', 'hobo2.swf', 'hobo3.swf', 'hobo4.swf', 'hobo5.swf', 'hobo6.swf', 'hobo7.swf', 'houseofwolves.swf', 'interactivebuddy.swf', 'jacksmith.swf', 'jellytruck.swf', 'johnnyupgrade.swf', 'jumpix2.swf', 'knightmaretower.swf', 'learn2fly.swf', 'learn2fly2.swf', 'learn2fly3.swf', 'magnetface.swf', 'mariocombat.swf', 'marioracingtournament.swf', 'meatboy.swf', 'megamanprojectx.swf', 'metroidelements.swf', 'mineblocks.swf', 'minesweeper.swf', 'mirrorsedge.swf', 'moneymovers.swf', 'moneymovers3.swf', 'motherload.swf', 'motox3m.swf', 'multitask.swf', 'mutilateadoll2.swf', 'myangel.swf', 'nanotube.swf', 'newgroundsrumble.swf', 'ngame.swf', 'nitromemustdie.swf', 'nucleus.swf', 'nv2.swf', 'nyancatlostinspace.swf', 'offroaders.swf', 'onemanarmy2.swf', 'outofthisworld.swf', 'pacman.swf', 'pandemic.swf', 'pandemic2.swf', 'papalouie.swf', 'papalouie2.swf', 'papalouie3.swf', 'picosschool.swf', 'picosschool2.swf', 'pirates.swf', 'polarjump.swf', 'portal.swf', 'portal2d.swf', 'quadrobarreldefence.swf', 'qubeythecube.swf', 'qwop.swf', 'raftwars.swf', 'raftwars2.swf', 'raze.swf', 'redball.swf', 'redball2.swf', 'redball4.swf', 'redball4v2.swf', 'redball4v3.swf', 'redshift.swf', 'revenant2.swf', 'riddleschool1.swf', 'riddleschool2.swf', 'riddleschool3.swf', 'riddleschool4.swf', 'riddleschool5.swf', 'riddletransfer.swf', 'riddletransfer2.swf', 'run2.swf', 'run3.swf', 'saszombieassault3.swf', 'sentryknight.swf', 'shoppingcarthero3.swf', 'siftheads.swf', 'siftheads2.swf', 'siftheads3.swf', 'siftheads4.swf', 'siftheads5.swf', 'sniperassassin4.swf', 'sportsheadsfootball.swf', 'sportsheadsracing.swf', 'sportsheadstennis.swf', 'stickrpg.swf', 'stickrun2.swf', 'stickwar.swf', 'strikeforceheroes2.swf', 'strikeforcekittylaststand.swf', 'sugarsugar.swf', 'sugarsugar2.swf', 'sugarsugar3.swf', 'superd.swf', 'superfighters.swf', 'supermario63.swf', 'supermarioflash.swf', 'supermarioflash2.swf', 'supersmashflash.swf', 'swordsandsandals2.swf', 'tacticalassassin.swf', 'tanks.swf', 'tanktrouble.swf', 'tetris.swf', 'thebindingofisaac.swf', 'thegame.swf', 'theimpossiblequiz.swf', 'theimpossiblequiz2.swf', 'theworldshardestgame2.swf', 'thingthingarena.swf', 'thisistheonlylevel.swf', 'tosstheturtle.swf', 'truckloader4.swf', 'ultimateflashsonic.swf', 'ultimatetactics.swf', 'unrealflash.swf', 'vex.swf', 'vex2.swf', 'vex3.swf', 'warp.swf', 'xenos.swf', 'xtremecliffdiving.swf', 'yearofthesnake.swf', 'yuriusshouseofspooks.swf', 'zombiealienparasites.swf']
flash_2 = []

def splitUpStr(s, indices):
	indices.insert(0, 0)
	return [s[i:j] for i, j in zip(indices, indices[1:] + [None])]

def genRandom(count, cap):
	randoms = []
	for x in range(0, count):
		randoms.append(random.randint(1, cap - 1))
	randoms.sort()
	return randoms

def insertBreaks(s):
	length = len(s)
	return breaker.join(splitUpStr(s, genRandom(math.ceil(length / breakerFrequency), length)))

# Generate HTML code for flash list
for x in range(0, len(flash_1)):
	flash_2.append(alist % insertBreaks(os.path.splitext(flash_1[x])[0].capitalize()))

# Write to list file
with open(outindex, "w") as file:
	file.write("\n".join(flash_2))

print("\nDone!")