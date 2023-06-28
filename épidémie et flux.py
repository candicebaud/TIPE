##data

NOM_PAYS = ["France", "Espagne", "Allemagne", "UK", "Italie", "Pologne", "Belgique", "Grèce", "Reptchèque", "Portugal", "Hongrie", "Suède", "Autriche", "Suisse", "Danemark", "Finlande", "Slovaquie","Norvège","Irlande", "Pays-Bas", "Algérie", "Arabie Saoudite", "Israel", "Malte", "Maroc", "Tunisie", "Egypte", "Turquie", "Canada", "USA", "Argentine", "Roumanie", "Kazakhstan", "Russie", "Ukraine", "Chine", "Inde"]

AFFICHER = ["évolution du nombre total de morts", "évolution du nombre de contaminés", "évolution des stocks en dollar usd", "évolution du nombre de vivants", " évolution des exports", "évolution du taux de contaminés", " évolution des imports"]

AFFICHERBIS=["évolution du nombre total de morts en fonction du temps ", "évolution du nombre de contaminés en fonction du temps", "évolution des stocks en dollar usd en fonction du temps", "évolution du nombre de vivants en fonction du temps", " évolution des exports en fonction du temps", "évolution du taux de contaminés en fonction du temps", " évolution des imports en fonction du temps"]

#données relatives aux pays (nombre hab, production 2017, consommation par habitant, numéro du pays, quantité exportée par an)
#production en dollars usd DE CEREALES par an

#AFNMO où on a de la donnée:
algerie=[42230000,1217055450, 0.393750627, 20, 0]
arabiesaoudite=[34813900,591101519, 0.393750627, 21, 0]
israel=[8655540, 125803727, 0.393750627, 22, 0]
malte=[514564, 12295953, 0.393750627, 23, 0]
maroc=[34660000, 2350715863, 0.393750627, 24, 0]
tunisie=[11180000,354334516, 0.393750627, 25, 0]
egypte=[102334000, 4303123738, 0.393750627, 26,0]
turquie=[84339100, 8556108904, 0.393750627, 27, 185858000]
AFNMO=[algerie, arabiesaoudite, israel, malte, maroc, tunisie, egypte, turquie]

#europe
france=[66352469, 12366941872, 0.393750627, 0, 5602340000]
espagne=[46439864, 3547151265, 0.393750627, 1, 0]
allemagne=[81174000, 8131825487, 0.393750627, 2, 2512970000]
UK=[64767115, 4359410688, 0.393750627, 3, 438740000]
italie=[60795612, 4301291729, 0.393750627, 4, 0]
pologne=[38005614, 5429724123, 0.393750627, 5, 978450000]
belgique=[11258434, 460108034, 0.393750627, 6, 0]
grece=[10812467,877721695, 0.393750627, 7, 0]
reptcheque=[10538275, 1389583863, 0.393750627, 8, 0]
portugal=[10374822, 253498428, 0.393750627, 9, 0]
hongrie=[9849000, 2311067527, 0.393750627, 10, 1747190000]
suede=[9747355, 983369105, 0.393750627, 11, 0]
autriche=[8584926, 708800003, 0.393750627, 12, 0]
suisse=[8236573,400991999, 0.393750627, 13, 0]
danemark=[5659715, 1776259292, 0.393750627, 14, 0]
finlande=[5471553, 565659239, 0.393750627, 15, 0]
slovaquie=[5421349, 59431977, 0.393750627, 16, 0]
norvege=[5165802, 459500938, 0.393750627, 17, 0]
irlande=[4625885, 344572386, 0.393750627, 18, 0]
paysbas=[16900726, 252251731, 0.393750627, 19, 0]
europe=[france, espagne, allemagne, UK, italie, pologne, belgique, grece, reptcheque, portugal, hongrie, suede, autriche, suisse, danemark, finlande, slovaquie, norvege, irlande, paysbas]

#autres pays importants
canada=[37590000,9711442097, 0.393750627, 28, 6305310000]
USA=[328200000,68607473570, 0.393750627, 29,18740200000]
argentine=[44490000,8846326657, 0.393750627, 30, 7511940000]
roumanie=[19410000,5391922117, 0.393750627,31, 2184270000]
kazakhstan=[18280000,2763295937, 0.393750627, 32, 852409000]
russie=[144500000,19082405580, 0.393750627, 33, 8142170000]
ukraine=[41980000,8391279873, 0.393750627, 34, 7947470000]
chine=[1393000000,2.62353E+11, 0.393750627, 35, 721030000]
inde=[1353000000,1.12689E+11, 0.393750627, 36, 7554560000]
autres=[canada, USA, argentine, roumanie, kazakhstan, russie, ukraine, chine, inde]

monde=[france, espagne, allemagne, UK, italie, pologne, belgique, grece, reptcheque, portugal, hongrie, suede, autriche, suisse, danemark, finlande, slovaquie, norvege, irlande, paysbas,algerie, arabiesaoudite, israel, malte, maroc, tunisie, egypte, turquie,canada, USA, argentine, roumanie, kazakhstan, russie, ukraine, chine, inde]

##exports data
exportsfrance=[10.46140423199625, 20, 2.59628620601895, 21, 0.22394042337746317, 22, 0.024384925299463987, 23,2.461897838345699, 24, 1.1658194663411847, 25, 0.7627146474383644, 26, 0.1740402455860384, 27, 0.0, 0, 11.60814377532809, 1, 6.408126274848944, 2, 2.909145701872827, 3, 5.703404947900281, 4, 0.6288688368175116, 5, 13.64848985498942, 6, 0.5503789165705348, 7, 0.207588356659343, 8, 3.0381989251974932, 9, 0.46307244422208316, 10, 0.11401233614984244, 11, 0.34679945368724713, 12, 0.8546931388491361, 13, 0.30463071389250035, 14,0.011785544860433152, 15, 0.05442148656141191, 16, 0.017798885524516053, 17, 0.7045103325393965, 18, 9.489925687618346, 19, 0.002637430115825833, 28, 0.05032216660995689, 29, 0.0005274860231651666, 30,0.40878659692377084, 31, 0.008319208136776342, 32, 0.3686524460755183, 33, 0.3207567151721212, 34, 0.6010929299405573, 35, 0.03018727155428082, 36] #export par personne
exportsespagne=[0]*74
exportsallemagne=[0.5889693744302363, 20,5.938859733412176, 21, 0.18519476679725036, 22, 0.0020942666371005494, 23, 0.5850025870352576,24, 0.0, 25, 0.0, 26, 0.2414812624732057, 27, 1.6679355458644394,0, 0.952509424199867, 1, 0.0, 2,0.7528642176066228, 3, 1.1632296055387192, 4,0.9158228004040703, 5, 3.1513292433537834, 6, 0.09580653903959396, 7,0.09580653903959396, 8, 0.7167565969399069, 9, 0.057629290166802176, 10, 0.12348781629585828, 11,0.5125655998226033,12, 0.6984009658264961, 13, 0.4261832606499618, 14,0.016212087614260722, 15,0.028346514893931554, 16, 0.25333234779609237, 17, 0.03783231083844581, 18, 5.927218074753, 19,0.0035232956365338656, 28, 0.1677877152782911, 29, 4.927686204942469e-05, 30, 0.01740705151895927, 31, 0.0002710227412718358, 32, 0.043437553896567865, 33, 0.037684480252297536, 34, 0.009313326927341267, 35, 0.0, 36]
exportsUK=[0.06600571910606177, 20, 0.008507403795892406, 21, 0.35135114479006824, 22, 0.014096660010253661, 23, 0.0, 24,0.0702825809054487, 25, 1.5439934293815618e-05, 26, 0.0035511848875775924, 27, 0.2991332870083838, 0, 1.0207494960984445, 1, 0.4161216691526248, 2, 0.0, 3, 0.16358610384297648, 4, 0.014266499287485633, 5,0.8785785811209902, 6, 0.06625275805476283, 7, 0.011965949077707105, 8, 0.4695129619406392, 9,0.0022542304068970806,10, 0.04000486975527627,11, 0.010900593611433827, 12, 0.005681895820124148, 13,0.02011823438484175, 14,0.006052454243175723, 15, 0.0007256769118093341, 16, 0.02118358985111503, 17,1.469295027268082, 18, 1.0202554182010424, 19, 0.10130140890172427, 28, 0.19211910241794775, 29, 0.00010807954005670933, 30, 0.0002933587515824968, 31, 0.0, 32,0.0, 33, 0.0, 34, 0.005975254571706645, 35,7.71996714690781e-05, 36]
exportsitalie=[0]*74
exportspologne=[0.15589802075030285,20,2.5434926534800884, 21, 0.0, 22, 0.05988588948990536, 23, 5.2623804472676064e-05, 24, 0.0, 25,1.4206585374465994, 26, 0.2910622625383713, 27, 0.10569491128336987, 0, 1.547192475301149, 1, 9.243608062745677, 2, 0.9485966994244587, 3, 0.334161158401493, 4, 0.0, 5, 0.06625336983109917, 6, 0.31953174075808904, 7, 0.5947805500524213, 8, 0.3518953805087848, 9, 0.12716542350822171, 10, 0.18860371523007102, 11, 0.06609549841768113, 12, 0.026048783213974653, 13, 0.4116760223897448, 14, 0.08803962488278705, 15, 0.09448604093068987, 16,0.3983095760536851, 17, 0.03773126780690874, 18, 1.0172444523590647, 19, 0.0030521806594152115, 28, 0.007577827844065353, 29, 0.0, 30, 0.05717576355956254, 31, 0.0, 32, 0.028864156753262822, 33, 0.007946194475374086,34, 0.0, 35, 0.0, 36]
exportsbelgique=[0]*74
exportsgrece=[0]*74
exportsreptcheque=[0]*74
exportsportugal=[0]*74
exportshongrie=[0.030663011473246016, 20, 2.659660879277084, 21, 0.032389075032998274, 22, 0.07533759772565743, 23, 1.427251497613971,24, 0.0, 25, 0.0, 26, 3.052695705147731, 0,0.6209767489085186, 1, 11.790537110366534, 2, 0.08437404812671337, 3, 57.27058584627881, 4, 4.7326632145395475, 5, 0.7912478424205504, 6, 3.1041730124885776, 7, 1.598334856330592, 8, 0.02832774901005178, 9, 0.0, 10, 0.0,11,1.6961315869631435, 12, 1.7761194029850746, 13, 0.01015331505736623, 14, 0.0018275967103259215,15,5.084069448674993, 16, 0.0031475276677835314, 17, 0.013808508478018074, 18,2.8561275256371204, 19, 0.0005076657528683116, 28, 0.007107320540156361, 29, 0.0, 30, 28.19768504416692, 31,0.04457305310183775, 32,8.774291806274748, 33, 5.544623819677125, 34, 0.005787389582698751, 35, 0.0, 36]
exportssuede=[0]*74
exportsautriche=[0]*74
exportssuisse=[0]*74
exportsdanemark=[0]*74
exportsfinlande=[0]*74
exportsslovaquie=[0]*74
exportsnorvege=[0]*74
exportsirlande=[0]*74
exportspaysbas=[0]*74
exportsalgerie=[0]*74
exportsarabiesaoudite=[0]*74
exportsisrael=[0]*74
exportsmalte=[0]*74
exportsmaroc=[0]*74
exportstunisie=[0]*74
exportsegypte=[0]*74
exportsturquie=[8.29982771929034e-05, 20, 0.01815290891176216, 21, 0.26981554225738713, 22,0.010825346725302974, 23, 0.0, 24, 0.006888857007010983, 25, 0.0, 26, 0.030294371175409746, 0, 0.013493148492217727, 1, 0.051399647375890894, 2, 0.13569032631365524, 3, 0.06854472006459637, 4, 0.0, 5, 0.03414786261650883, 6, 0.010517067410015046, 7, 0.0006995569077687573, 8, 0.0, 9, 0.014595839889209157, 10, 0.002525519006012632, 11, 0.005821736300245082, 12, 0.00815754495838822, 13, 0.0002134241413531802, 14,0.0004031344892226737, 15, 0.0, 16, 0.002715229353882126, 17, 4.742758696737338e-05, 18, 0.0194215968631394, 19, 0.04470050071674941, 28, 0.6195702823482822, 29, 0.0, 30, 0.009604086360893108, 31, 0.006758431142850707, 32, 0.0038653483378409304, 33, 0.017334783036574968, 34, 1.1856896741843345e-05, 35, 0.0007825551849616607, 36]
exportscanada=[8.608273476988561, 20, 0.9110667730779463, 21, 0.006517690875232775, 22, 0.014285714285714285, 23, 5.052274541101356, 24, 0.5281989890928438, 25, 0.04732641660015962, 26, 0.9531258313381218, 27, 0.281511040170258, 0, 1.1488427773343974, 1, 0.2590316573556797, 2, 3.086778398510242, 3, 5.02487363660548, 4, 0.0, 5, 1.3740888534184623, 6, 0.012396914072891726, 7, 0.0, 8, 0.7461558925246076, 9, 0.0, 10, 0.003378558127161479, 11, 0.005826017557861133, 12, 0.4795424314977388, 13, 0.0027400904495876563, 14, 2.6602819898909284e-05, 15, 0.0, 16, 0.0003192338387869114, 17, 1.7341846235700984, 18, 0.6632349028997073, 19, 0.0, 28, 28.00053205639798, 29, 0.00023942537909018357, 30, 0.0, 31, 0.0, 32, 0.0022346368715083797, 33, 0.0, 34, 11.695956371375365, 35, 0.0031391327480712957, 36]
exportsUSA=[0.5279128580134065, 20, 1.1996739792809263, 21, 0.20313223644119438, 22, 0.0007099329677026203, 23, 0.5454478976234004, 24, 0.009926873857404022, 25, 0.19794028031687996, 26, 0.10457647775746497, 27, 0.0769926873857404, 0, 0.1509354052407069,1, 0.033769043266301035, 2, 0.18576782449725776, 3, 0.4285588056063376, 4, 0.004722730042656917, 5, 0.018598415600243754, 6, 0.004567336989640463, 7, 6.093845216331505e-05, 8, 0.060856185252894573, 9, 0.0015234613040828763, 10, 0.012635588056063376, 11, 0.006380255941499086, 12, 0.008488726386349787, 13, 0.005551492992078001, 14, 0.0017032297379646556, 15, 0.0, 16, 0.006733698964046313, 17, 0.05971358927483242, 18, 0.12470444850700792, 19, 1.5059689213893968, 28, 0.0, 29, 0.005730652041438147, 30, 0.0005971968312004875, 31, 0.0006703229737964656, 32, 0.010923217550274223, 33, 0.01064594759293114, 34, 4.107876294942108, 35, 0.015426569165143206, 36]
exportsargentine=[19.821532928748034, 20, 8.547336480107889, 21, 0.022454484153742415, 22, 0.0, 23, 5.671813890761969, 24, 1.1792312879298719, 25, 11.572285906945382, 26, 0.05945156214879748, 27, 0.03387278040008991, 0, 0.42063385030343897, 1, 0.11254214430209036, 2, 0.5785569790964261, 3, 0.045830523713193974, 4, 0.2454484153742414, 5, 0.040908069229040236, 6, 0.012587098224320073, 7, 0.007956844234659474, 8, 0.003888514272870308, 9, 0.0, 10, 0.0, 11, 0.0006293549112160036, 12, 0.14661721735221397, 13, 0.02775904697684873, 14, 0.0, 15, 8.990784445942908e-05, 16, 0.0007866936390200045, 17, 0.0010114632501685772, 18, 0.15014610024724656, 19, 0.04236907170150596, 28, 2.0945830523713194, 29, 0.0, 30, 0.008676106990334907, 31, 0.0, 32, 0.022252191503708697, 33, 0.0005169701056417172, 34, 0.004495392222971455, 35, 0.8626432906271072, 36]
exportsroumanie=[0.119629057187017, 20, 5.6155074703760945, 21, 0.0008758371973209686, 22, 0.37980422462648117, 23, 3.6187017001545594, 24, 0.9254507985574446, 25, 12.294178258629572, 26, 3.8095311695002576, 27, 1.6410097887686759, 0, 1.3582689335394127, 1, 0.767284904688305, 2, 2.2951056156620298, 3, 7.916486347243689, 4, 0.2605358062854199, 5, 0.9037609479649665, 6, 2.3135497166409067, 7, 0.1842864502833591, 8, 0.9379185986604843, 9, 1.735239567233385, 10, 0.43086038124678, 11, 1.7996908809891807, 12, 0.33369397217928903, 13, 0.0028851107676455437, 14, 0.0, 15, 0.23142709943328182, 16, 0.0068006182380216385, 17, 0.19273570324574962, 18, 1.3801648634724368, 19, 0.10664605873261206, 28, 0.42416280267903145, 29, 0.0, 30, 0.0, 31, 0.00844925296239052, 32, 2.060226687274601, 33, 2.2080886141164346, 34, 0.0, 35, 0.0, 36]
exportskazakhstan=[0.15421225382932166, 20, 0.0, 21, 0.0, 22, 0.0, 23, 0.0, 24, 0.22401531728665208, 25, 0.06602844638949672, 26, 1.7224835886214442, 27, 0.0, 0, 0.0, 1, 0.03025164113785558, 2, 0.2799781181619256, 3, 2.938074398249453, 4, 0.05300875273522976, 5, 0.38938730853391684, 6, 0.0, 7, 0.0007658643326039387, 8, 0.0, 9, 0.0, 10, 0.36504376367614877, 11, 0.0, 12, 0.013074398249452954, 13, 0.0, 14, 0.12784463894967177, 15, 0.0,16, 0.013457330415754924, 17, 0.0, 18, 0.006181619256017505, 19, 0.225054704595186, 28, 0.0004923413566739606, 29, 0.0, 30, 0.0, 31, 0.0, 32, 1.886159737417943, 33, 0.2400437636761488, 34, 3.09753829321663, 35, 0.0, 36]
exportsrussie=[0.11103806228373703, 20, 1.9170795847750866, 21, 0.0, 22, 0.5084152249134948, 23, 0.39909342560553634, 24, 10.573314878892733, 25, 5.25235294117647, 26, 0.02085121107266436, 0, 0.06303114186851211, 1, 0.1391833910034602, 2, 0.32438754325259517, 3, 0.2810242214532872, 4, 0.01330795847750865, 5, 0.05903114186851211, 6, 0.30187543252595156, 7, 0.0002837370242214533, 8, 0.0, 9, 0.002304498269896194, 10, 0.01613840830449827, 11, 0.0031903114186851212, 12, 0.01536332179930796, 13, 0.08107266435986159, 14, 0.0008512110726643598, 15, 0.0, 16, 0.07142560553633218, 17, 0.0752318339100346, 18, 0.393038062283737, 19, 0.021833910034602076, 28, 0.01469204152249135, 29, 0.0, 30, 0.01843598615916955, 31, 0.0980553633217993, 32, 0.0, 33, 0.06280968858131487, 34, 0.04119031141868512, 35, 0.6239861591695501, 36]
exportsukraine=[1.398808956646022, 20, 9.371605526441163, 21, 0.18997141495950454, 22, 0.03277751310147689, 23, 3.2256312529776086, 24, 7.072439256788947, 25, 25.496236303001428, 26, 3.9179371129109097, 27, 0.08151500714626013, 0, 12.631729394949977,1, 1.0134111481657933, 2, 1.6448785135778943, 3, 8.731038589804669, 4, 0.7002382086707957, 5, 2.1504287756074323, 6, 0.7276560266793711, 7, 0.021676989042401142, 8, 3.0632682229633157, 9, 0.05452596474511672, 10, 0.027489280609814197, 11, 0.1316579323487375, 12, 0.07532158170557408, 13, 0.06476893758932825, 14, 0.003358742258218199, 15, 0.0013577894235350166, 16, 0.0020009528346831827, 17, 0.7855645545497856, 18, 11.760576464983325, 19, 0.012148642210576465, 28, 0.0034778465936160076, 29, 0.0, 30, 0.09299666507860886, 31, 0.0031205335874225824, 32, 0.49187708432586946, 33, 0.0, 34, 12.348451643639828, 35, 12.067651262505954, 36]
exportschine=[0.00016941852117731515, 20, 0.0005190236898779613, 21, 8.183776022972003e-05, 22, 2.871500358937545e-05, 23, 9.834888729361091e-05, 24, 3.589375448671931e-06, 25, 0.0001830581478822685, 26, 0.005466618808327351, 27, 0.0010244077530509692, 0, 0.0002390524048815506, 1, 0.001256281407035176, 2, 0.0006898779612347451, 3, 0.00022613065326633166, 4, 6.460875807609476e-06, 5, 0.00013854989231873655, 6, 2.871500358937545e-05, 7, 5.0251256281407036e-05, 8, 1.7946877243359657e-05, 9, 7.178750897343862e-07, 10, 9.117013639626705e-05, 11, 4.3072505384063175e-05, 12,2.4407753050969132e-05, 13, 1.8664752333094043e-05, 14, 2.871500358937545e-06, 15, 0.00029576453697056714, 16, 2.08183776022972e-05, 17, 8.399138549892319e-05,18, 0.0016611629576453698, 19, 0.003267767408470926, 28, 0.007354630294328787, 29, 0.0, 30, 0.0, 31, 2.153625269203159e-06, 32, 0.0021586503948312994, 33, 0.0,34, 0.0, 35, 7.394113424264179e-05, 36]
exportinde=[0.017706577974870658, 20, 0.5929563932002956, 21, 0.01785957132298596, 22, 0.00020620842572062085, 23, 0.0012483370288248338, 24, 0.007502586844050259, 25, 0.03042867701404287, 26, 0.006866962305986696, 27, 0.04589578713968958, 0, 0.0034789356984478935, 1, 0.025127864005912787, 2, 0.1392239467849224, 3, 0.03618255728011826, 4, 0.0066585365853658535, 5, 0.020244641537324463, 6, 0.002588322246858832, 7, 0.0013325942350332594, 8, 0.005578713968957871, 9, 0.00014412416851441242, 10, 0.0058307464892830745, 11, 0.006283074648928307, 12, 0.005977827050997783, 13, 0.0007730968218773097, 14, 0.0004449371766444937, 15, 4.7302291204730226e-05, 16, 0.0002992609016999261, 17, 0.0012985957132298595, 18, 0.03643385070214338, 19, 0.03851810790835181, 28, 0.12163266814486327, 29, 0.0001500369549150037, 30, 0.00011677753141167775, 31, 0.0005018477457501847, 32, 0.019248337028824832, 33, 0.008032520325203253, 34, 5.764966740576497e-05, 35, 0.0, 36]


exports=[exportsfrance, exportsespagne, exportsallemagne, exportsUK, exportsitalie, exportspologne, exportsbelgique, exportsgrece, exportsreptcheque,exportsportugal, exportshongrie, exportssuede,exportsautriche,exportssuisse,exportsdanemark, exportsfinlande, exportsslovaquie, exportsnorvege, exportsirlande, exportspaysbas, exportsalgerie, exportsarabiesaoudite, exportsisrael, exportsmalte, exportsmaroc, exportstunisie, exportsegypte, exportsturquie, exportscanada, exportsUSA, exportsargentine, exportsroumanie, exportskazakhstan, exportsrussie, exportsukraine, exportschine, exportinde]

import numpy as np
import matplotlib.pyplot as plt
import random as rd
from math import floor
from math import ceil

##liste avec les numéros des pays concernés
def listenum(H):
    listenum=[0]*(len(H))
    for i in range (len(H)):
        listenum[i]=H[i][1]
    return (listenum)

##creerseuildepart
def seuildep(T, sc, sd, S):
    for i in range (len(T)):
        if S[i]==0:
            if T[i]>=sc:
                S[i]=1
            else:
                S[i]=0
        else:
            if T[i]>sd:
                S[i]=1
            else:
                S[i]=0
    return S

##taux
def taux(C, L):
    T=[0]*(len(C))
    for i in range (len(C)):
            if (L[i][0]+L[i][1]+L[i][2])==0:
                T[i]=0
            else:
                T[i]=(L[i][1])/(L[i][0]+L[i][1]+L[i][2])
    return (T)

def tauxlocal(C, L, i):
    T=0
    if (L[i][0]+L[i][1]+L[i][2])==0:
        T=0
    else:
        T=(L[i][1])/(L[i][0]+L[i][1]+L[i][2])
    return (T)

##creertableau
def creertableau(n, a):
    N=[0]*n
    for i in range (n):
        N[i]=[0]*a
    return N

##SIRevol
#Lt=[St, It, Rt, Dt] #D les dead
#d le taux de létalité =! taux de mortalité
def SIRevol(Lt, beta, i, k): # Lt la liste au temps t, L1 la liste au temps t+1, beta param de l'épidémie
#modèle d'évolution de t à t+1
    gamma=0.2
    d=0.048
    N=(Lt[0]+Lt[1]+Lt[2]+Lt[3])
    if N==0:
        return ([0, 0, 0, 0])
    else:
        L1=[0,0,0,0]
        L1[0]= (-beta[i][k]*Lt[0]*Lt[1])/(N) +Lt[0] #St+1
        L1[1]= beta[i][k]*Lt[0]*Lt[1]/(N) - gamma*Lt[1] +Lt[1] -d*Lt[1] #It+1
        L1[2]= Lt[2]+ gamma*Lt[1] #Rt+1
        L1[3]= Lt[3]+d*Lt[1]
        Lt=L1 #Lt devient L1 pour pouvoir ensuite le faire à chaque temps
        return (Lt) #on renvoie la liste au temps t+1


##renvoyer une case
def case(Lt,n):
    return (Lt[n])

##creerLt pour le début seulement
def creerLt(C, H, i): #crée un Lt pour le pays en position i
    Lt=[0, 0, 0, 0]
    Lt[0]=H[i][0]-C[i]
    Lt[1]=C[i]
    return Lt

##creerL au depart
def creerL(C, H): #crée la liste des Lt-> cad on a L[0][0] qui donne le nombre de sains dans le pays 0
#L[0][1] le nombre de contaminés du pays 0
#L[0][2] le nombre de recovered du pays 1
    L=creertableau(len(C), len(C))
    for i in range (len(C)):
        L[i]=creerLt(C,H,i)
    return L

##verifS
def verifS(S):
    n=len(S)
    res=0
    for i in range (n):
        if S[i]==1:
            res=res+1
    if res==n:
        return False

##creerV V=voyageurs en prenant en compte les stratégies de confinement

def creerV(L, C, S, Pop):
    paspossible=[]
    for i in range (len(C)):
        if Pop[i]==0:
            paspossible.append(i) # on fait la liste des gens qui ne peuvent pas voyager car ils sont morts
    V=[0]*(len(C))
    for i in range (len(C)):
            V[i]=[0]*2
    if verifS(S)==False:
        for i in range (len(C)):
            V[i][0]=0
    else :
        for i in range (len(C)):
            if S[i]==0:
                V[i][1]= rd.randint(0,(len(C)-1))
                while S[V[i][1]]==1 :
                    V[i][1]=rd.randint(0, len(C)-1)
                    while V[i][1] in paspossible :
                        V[i][1]=rd.randint(0, len(C)-1)
                V[i][0]=rd.uniform(0, 0.0002)*(L[i][0]+L[i][1]+L[i][2])#on ne veut pas que plus de la moitié de la population se barre sinon pas cohérent
            else:
                V[i][0]=0
    return (V)

##creerD
def creerD(H, C, V, L): #on renvoie la liste des contaminés qui se déplacent et où ils se déplacent
    D=[0]*(len(C))
    T=taux(C, L)
    for i in range (len(C)):
        D[i]=[0]*2
    for i in range (len(C)):
        D[i][0]=(V[i][0]*T[i])
        D[i][1]=V[i][1]
    return (D)

##creerE
def creerE(H, S, E, exports, Pop):
    paspossible=[]
    for i in range (len(H)):
            if Pop[i]==0:
                paspossible.append(i)
    if verifS(S)==False:
        for i in range (len(E)):
            for k in range (len(E[i])):
                E[i][k]=0
    else:
        for i in range (len(E)):
            if S[i]==0:
                for k in range (len(E[i])):
                    if k%2==0:
                        E[i][k]=exports[i][k]*Pop[i]/365
                    else:
                        if k in paspossible:
                            E[i][k-1]=0
                        else:
                            E[i][k]=exports[i][k]

            else:
                for k in range (len(E[i])):
                    E[i][k]=0
    return E

##trouver les contaminés
def recherche(D, i):
    c=0 #res
    for k in range (len(D)):
        if D[k][1]==i:
            c=c+D[k][0]
    return c

def recherchebis(E,H,i):
    c=0
    for k in range (len(E)):
        for a in range (len(E[i])):
            if a%2==1:
                if E[k][a]==H[i][3]:
                    c=c+abs(E[k][a-1])
    return c

##creer beta
def creertableaubeta(n,C):
    beta=creertableau(len(C), n+1)
    for i in range (len(C)):
        beta[i][0]=0.39
    return beta

##creerZ
def creerZ(H, prop):
    Z=[0]*len(H)
    for i in range (len(Z)):
        Z[i]=H[i][1]*prop
    return Z

##faire manger les gens
def manger(Pop, Z, i, L):
    consoparhab=0.393750627
    viv=Pop[i] # nos vivants avant de voir qui aura assez à manger
    ts=0
    tc=0
    tr=0
    survivants=0
    capacité=0
    nouveauxmorts=0
    if Pop[i]!=0:
        ts=L[i][0]/viv
        tc=L[i][1]/viv
        tr=L[i][2]/viv
        capacité=Z[i]//consoparhab
        if capacité<viv:
            survivants=capacité
            nouveauxmorts=viv-survivants
            Pop[i]=survivants
            L[i][0]=ts*Pop[i]
            L[i][1]=tc*Pop[i]
            L[i][2]=tr*Pop[i]
            L[i][3]=L[i][3]+nouveauxmorts
            Z[i]=0
        else:
            Z[i]=Z[i]-Pop[i]*consoparhab

    return (Z[i], L[i])


##expansion avec confinement
def expansionconfined(C, H, n, sc, sd, exports, prop):# d le taux de gens qui meurent
    Pop=[0]*len(H)
    for i in range (len(H)):
        Pop[i]=H[i][0]
    L=creerL(C, H)
    beta=creertableaubeta(n, C)
    gamma=0.2
    d=0.048
    S=[0]*(len(C))
    T=taux(C,L)
    evoltaux=creertableau(len(C), n)
    Z=creerZ(H, prop)
    E=creertableau(len(C), len(exports))
    S=seuildep(T,sc, sd,S)
    V=creerV(L,C,S, Pop)
    D=creerD(H,C,V,L) #D le tableau des gens dangereux qui se déplacent et vers quel pays ils se déplacent
    evolcontamines=creertableau(len(C), n) #evolution des contaminés
    evolmorts=creertableau(len(C),n)
    evoldeZ=creertableau(len(C), n)
    evoldeE=creertableau(len(C), n)
    evolimports=creertableau(len(C),n)
    evoldeH=creertableau(len(C), n)
    listedeS=creertableau(len(C),n)
    prodpartravailleurparjour=[]
    for i in range (len(C)):
        evoldeZ[i][0]=Z[i]
        evolmorts[i][0]=0
        evoldeH[i][0]=Pop[i]
        evoldeE[i][0]=0
        evoltaux[i][0]=T[i]
        evolimports[i][0]=0
        listedeS[i][0]=S[i]
    for i in range (len(H)):
        prodpartravailleurparjour.append(H[i][1]/H[i][0]/365)
    for k in range (1, n):
        T=taux(C,L)
        S=seuildep(T,sc, sd ,S)
        V=creerV(L,C,S, Pop)
        D=creerD(H,C,V,L)
        E=creerE(H, S, E, exports, Pop)
        for i in range (len(C)):
            #partie épidémiologique
            L[i]=SIRevol(L[i], beta, i, k)
            C[i]=L[i][1] + recherche(D,i)-D[i][0] #on contamine
            Pop[i]=Pop[i]+recherche(V,i)-V[i][0]
            L[i]=[Pop[i]-C[i]-L[i][2],C[i],L[i][2],L[i][3]]
            evolcontamines[i][k]=C[i]
            evolmorts[i][k]=L[i][3]
            listedeS[i][k]=S[i]
            if listedeS[i][k]==1:
                beta[i][k+1]=0.22
            else:
                beta[i][k+1]=0.39
            evoltaux[i][k]=tauxlocal(C,L, i)
            #partie échanges de céréales
            travailleurs=(L[i][0]+L[i][2])
            Z[i]=Z[i]+prodpartravailleurparjour[i]*travailleurs #on produit de la nourriture
            Z[i]=Z[i]+recherchebis(E,H,i)-E[i][0] #on importe et exporte
            Z[i]=manger(Pop, Z, i, L)[0]
            L[i]=manger(Pop, Z, i, L)[1]
            evolmorts[i][k]=L[i][3]
            evolcontamines[i][k]=L[i][1]
            evolmorts[i][k]=L[i][3]
            evoldeZ[i][k]=Z[i]
            evoldeH[i][k]=Pop[i]
            evoldeE[i][k]=somme3(E, i)
            evolimports[i][k]=recherchebis(E,H,i)


    return ([evolmorts, evolcontamines, evoldeZ, evoldeH, evoldeE, evoltaux, evolimports]) #on renvoie la liste des états de chaque pays


##tracer des évolutions en fonction
def tracercontamines(C, H, n,sc, sd):
    evol=expansionconfined(C, H, n, sc, sd)[1]
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    for k in range (len(C)):
        plt.plot(abscisse,evol[k], label=str(NOMS_PAYS[liste[k]]))
        plt.legend()
        plt.title("Nombre de contaminés en fonction du temps")
        plt.xlabel("Temps en jours")
        plt.ylabel("Nombre de contaminés")
        plt.legend(fontsize=6, loc='best')
    return(plt.show())

def tracermorts(C, H, n, sc, sd, exports, prop):
    evol=expansionconfined(C, H, n, sc, sd, exports, prop)[0]
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    for k in range (len(C)):
        plt.plot(abscisse,evol[k], label=str(NOM_PAYS[liste[k]]))
        plt.legend()
        plt.title("Nombre de morts en fonction du temps")
        plt.xlabel("Temps en jours")
        plt.ylabel("Nombre de morts")
        plt.legend(fontsize=6, loc='best')
    plt.show()

def touttracer(C, H, n, sc, sd, exports, prop):
    RES=expansionconfined(C, H, n, sc, sd, exports, prop)
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    for a in range (len(RES)):
        for k in range (len(liste)):
            plt.plot(abscisse, RES[a][k], label=str(NOM_PAYS[k]))
            plt.legend()
            plt.xlabel("temps en jour")
            plt.title(str(AFFICHERBIS[a]))
            plt.ylabel(str(AFFICHER[a]))
            plt.legend(fontsize=6, loc='best')
        plt.show()

def tracerfrance(C, H, n, sc, sd, exports, prop):
    RES=expansionconfined(C, H, n, sc, sd, exports, prop)
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    for a in range (len(RES)):
        for k in range (1):
            plt.plot(abscisse, RES[a][k], label=str(NOM_PAYS[k]))
            plt.legend()
            plt.xlabel("temps en jour")
            plt.title(str(AFFICHERBIS[a]))
            plt.ylabel(str(AFFICHER[a]))
            plt.legend(fontsize=6, loc='best')
        plt.show()

##somme
def somme3(E, i):
    s=0
    for k in range (len(E)):
        s=s+E[i][k]
    return (s)

##application A FAIRE
#touttracer([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10, 3, 0, 9, 0, 0, 0,1, 0, 20,65,0, 2, 0,0,0,32616,0],monde, 365, 0.003, 0.0006, exports, 30)

#touttracer([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10, 3, 0, 9, 0, 0, 0,1, 0, 20,65,0, 2, 0,0,0,32616,0],monde, 365, 0.003, 0.0006, exports, 1)

#tracerfrance(([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10, 3, 0, 9, 0, 0, 0,1, 0, 20,65,0, 2, 0,0,0,32616,0],monde, 365, 0.003, 0.0006, exports, 1)
