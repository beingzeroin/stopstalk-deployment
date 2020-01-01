"""
    Copyright (c) 2015-2020 Raj Patel(raj454raj@gmail.com), StopStalk

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

stable = db.submission
atable = db.auth_user
cftable = db.custom_friend
nrtable = db.next_retrieval

user_ids = [6683L, 4097L, 6146L, 4099L, 2052L, 4102L, 4103L, 4104L, 6153L, 4106L, 4107L, 6156L, 6157L, 2062L, 6159L, 2064L, 4114L, 6165L, 6171L, 4125L, 4126L, 2080L, 5808L, 4131L, 6181L, 6151L, 6190L, 2095L, 7176L, 6194L, 4148L, 2101L, 6198L, 2103L, 7829L, 5812L, 6495L, 2058L, 6207L, 6208L, 2114L, 6155L, 6213L, 6214L, 6215L, 12L, 4172L, 2128L, 5816L, 6226L, 2131L, 6158L, 6230L, 6233L, 6686L, 4189L, 4190L, 6239L, 6241L, 4195L, 6244L, 6245L, 3090L, 4207L, 4209L, 114L, 4211L, 4214L, 4215L, 120L, 6265L, 4799L, 4220L, 5652L, 7872L, 2179L, 7873L, 6280L, 4233L, 6378L, 2187L, 2190L, 144L, 7192L, 6294L, 6306L, 4259L, 925L, 7878L, 4263L, 7707L, 6725L, 4270L, 2223L, 4272L, 6321L, 2226L, 2227L, 5150L, 4809L, 4280L, 6330L, 3103L, 2236L, 4285L, 2239L, 4290L, 4811L, 6144L, 7201L, 716L, 203L, 204L, 7099L, 6350L, 2257L, 6354L, 5838L, 4311L, 2267L, 224L, 5840L, 6373L, 6375L, 6376L, 6377L, 7421L, 2283L, 236L, 2287L, 4343L, 6392L, 7987L, 2300L, 4351L, 6401L, 2308L, 4357L, 2312L, 2315L, 6412L, 5239L, 4366L, 6417L, 2464L, 4779L, 388L, 6428L, 3899L, 3120L, 290L, 4389L, 1073L, 6440L, 6443L, 2348L, 5853L, 4401L, 1075L, 3806L, 2358L, 4408L, 6457L, 2364L, 394L, 320L, 4419L, 5857L, 6472L, 6473L, 6353L, 4428L, 6477L, 334L, 6480L, 6482L, 5859L, 2057L, 7225L, 4441L, 4443L, 5861L, 4448L, 6497L, 2402L, 6499L, 6501L, 6545L, 360L, 6695L, 362L, 4460L, 6509L, 4463L, 368L, 6888L, 6515L, 6516L, 6518L, 4472L, 6521L, 4159L, 6529L, 7105L, 6532L, 389L, 5868L, 4490L, 395L, 6541L, 4495L, 401L, 4499L, 7995L, 409L, 6553L, 410L, 6555L, 2458L, 2462L, 6559L, 6560L, 6562L, 2467L, 4519L, 2472L, 5947L, 6572L, 754L, 2742L, 6577L, 6578L, 4531L, 4532L, 4510L, 4995L, 7924L, 444L, 6589L, 448L, 6593L, 451L, 6596L, 2501L, 6600L, 4553L, 6602L, 6604L, 7245L, 4561L, 2515L, 6614L, 4568L, 5744L, 6618L, 476L, 6621L, 6623L, 6224L, 4585L, 5267L, 6225L, 2537L, 2538L, 6635L, 4790L, 6568L, 2546L, 83L, 500L, 2551L, 3631L, 4602L, 6651L, 2556L, 7594L, 6655L, 2560L, 4609L, 6658L, 6659L, 6660L, 2134L, 7191L, 4524L, 4618L, 4620L, 2573L, 1995L, 4525L, 4624L, 4625L, 4626L, 6676L, 533L, 6680L, 6681L, 4635L, 6234L, 4638L, 4640L, 5610L, 3496L, 4645L, 2598L, 4529L, 6697L, 2604L, 4655L, 6704L, 2609L, 6707L, 2142L, 7799L, 4665L, 570L, 4668L, 6722L, 4675L, 4676L, 3510L, 2631L, 6728L, 2633L, 6731L, 6732L, 6734L, 6735L, 5268L, 596L, 6741L, 598L, 6743L, 4696L, 2377L, 6751L, 6752L, 4880L, 2661L, 4710L, 7953L, 1468L, 5950L, 4723L, 4725L, 4729L, 6779L, 6977L, 6784L, 5568L, 642L, 6934L, 6794L, 7523L, 652L, 6798L, 2703L, 6801L, 6804L, 6805L, 6806L, 6807L, 2112L, 666L, 4763L, 6812L, 6813L, 7621L, 6817L, 6818L, 6820L, 678L, 680L, 7524L, 3527L, 4780L, 6829L, 6830L, 7456L, 6833L, 2741L, 6838L, 4791L, 696L, 6843L, 4797L, 6847L, 4456L, 4807L, 2761L, 6859L, 6860L, 2850L, 4814L, 3533L, 6864L, 3570L, 4819L, 4824L, 2779L, 4833L, 4837L, 5412L, 4840L, 5244L, 2794L, 6891L, 2796L, 4845L, 750L, 1832L, 4850L, 4852L, 3198L, 4854L, 4860L, 4864L, 6504L, 6914L, 4867L, 4869L, 6921L, 2827L, 6924L, 784L, 6931L, 2836L, 2838L, 4887L, 3777L, 6939L, 2844L, 4894L, 4895L, 4896L, 6945L, 6946L, 4899L, 6951L, 6952L, 2859L, 812L, 6957L, 4910L, 5256L, 4914L, 6963L, 6965L, 6966L, 4919L, 4920L, 4575L, 5258L, 2878L, 832L, 4929L, 4930L, 835L, 6981L, 4577L, 4936L, 3212L, 4938L, 7723L, 4940L, 4941L, 6990L, 4943L, 6968L, 4963L, 7651L, 852L, 3214L, 3558L, 4951L, 1223L, 2906L, 2747L, 7005L, 2910L, 7803L, 4964L, 7013L, 871L, 4970L, 4972L, 7021L, 878L, 7997L, 7024L, 2929L, 7026L, 2931L, 7599L, 6633L, 7032L, 2937L, 7034L, 7035L, 7037L, 7039L, 1515L, 7044L, 903L, 5000L, 7049L, 5003L, 7052L, 7054L, 2962L, 7060L, 2967L, 920L, 7065L, 5021L, 928L, 7076L, 7665L, 5033L, 1054L, 5037L, 5039L, 5041L, 5042L, 7092L, 2998L, 6644L, 5050L, 5051L, 956L, 6986L, 5055L, 3009L, 7106L, 5060L, 5061L, 5062L, 7114L, 972L, 5282L, 7120L, 5073L, 5077L, 1188L, 3037L, 990L, 7135L, 7136L, 993L, 994L, 995L, 3044L, 3048L, 7676L, 8018L, 7150L, 7151L, 5104L, 7153L, 1010L, 4947L, 3060L, 5109L, 7159L, 1017L, 3583L, 7338L, 5973L, 5121L, 5974L, 3079L, 3080L, 5130L, 5975L, 5132L, 4610L, 3088L, 3089L, 7186L, 7188L, 5141L, 3095L, 5144L, 7195L, 3102L, 1055L, 5968L, 6309L, 3854L, 5157L, 5980L, 7687L, 7212L, 4957L, 1072L, 3592L, 5170L, 5171L, 5172L, 7221L, 3129L, 4264L, 3132L, 5181L, 3135L, 7240L, 7241L, 5197L, 1104L, 7251L, 5204L, 7253L, 1111L, 2675L, 5209L, 2015L, 7271L, 5224L, 6332L, 7274L, 6333L, 7281L, 5234L, 1141L, 3191L, 1145L, 1147L, 1148L, 1150L, 3199L, 7297L, 7298L, 4812L, 5253L, 3206L, 7303L, 7304L, 7306L, 7308L, 5262L, 5263L, 7312L, 5266L, 3219L, 7316L, 5269L, 7320L, 3227L, 5222L, 5281L, 7330L, 5283L, 5284L, 1189L, 7025L, 5289L, 5290L, 2247L, 7341L, 7343L, 7344L, 5297L, 5300L, 5301L, 7350L, 7353L, 5306L, 5307L, 5308L, 7361L, 4641L, 3275L, 1228L, 1230L, 5327L, 5329L, 7379L, 2254L, 5339L, 5669L, 1248L, 891L, 4305L, 1256L, 7401L, 7402L, 7403L, 7404L, 7406L, 5359L, 5364L, 7415L, 5368L, 1273L, 7418L, 7650L, 5674L, 7422L, 4782L, 7425L, 3627L, 5380L, 5381L, 5382L, 7431L, 5387L, 5390L, 7443L, 7444L, 438L, 7446L, 7447L, 7448L, 7450L, 7451L, 5408L, 5409L, 5410L, 219L, 7460L, 7461L, 4657L, 5704L, 5418L, 1324L, 5422L, 5426L, 5430L, 7479L, 5433L, 5841L, 5436L, 2806L, 1954L, 7489L, 3394L, 1347L, 7492L, 5445L, 5447L, 7496L, 3401L, 7498L, 7499L, 7501L, 5454L, 5458L, 7510L, 5464L, 7514L, 4069L, 7516L, 7522L, 5691L, 1380L, 6320L, 7532L, 7533L, 5486L, 5488L, 2280L, 7540L, 7541L, 7543L, 7544L, 5498L, 7743L, 7548L, 5501L, 7550L, 3989L, 7554L, 6379L, 7558L, 1417L, 3466L, 7565L, 7567L, 5520L, 7569L, 5522L, 6723L, 7573L, 1430L, 7748L, 6383L, 6799L, 3486L, 5535L, 1440L, 7588L, 7589L, 7590L, 1723L, 3497L, 1450L, 7751L, 1452L, 7598L, 7069L, 7601L, 3508L, 5558L, 7607L, 7608L, 7611L, 5564L, 5567L, 3520L, 7618L, 7619L, 3525L, 5574L, 5575L, 8028L, 7629L, 7630L, 3536L, 2296L, 7634L, 5587L, 7640L, 2980L, 7645L, 7646L, 3551L, 7648L, 3554L, 5603L, 7652L, 3557L, 7654L, 7656L, 252L, 3562L, 7079L, 3567L, 3569L, 7666L, 7670L, 5623L, 5624L, 7673L, 7675L, 1532L, 3581L, 5631L, 5635L, 3588L, 7685L, 4320L, 1543L, 7688L, 7691L, 7692L, 7693L, 7694L, 4013L, 3602L, 7699L, 7700L, 7701L, 6745L, 7705L, 7706L, 3611L, 8030L, 3614L, 2309L, 7713L, 7714L, 5668L, 7717L, 3624L, 7721L, 3626L, 5675L, 7724L, 3629L, 3677L, 1585L, 1587L, 5685L, 7734L, 5688L, 2029L, 7738L, 1595L, 7741L, 6069L, 3649L, 3652L, 5703L, 3656L, 3658L, 4023L, 3660L, 3661L, 7759L, 7762L, 5715L, 5716L, 7766L, 7767L, 1627L, 7773L, 7775L, 7778L, 5731L, 5169L, 5510L, 5736L, 7788L, 5742L, 5743L, 7792L, 7794L, 5750L, 5751L, 1656L, 7802L, 5755L, 5756L, 3709L, 6943L, 1665L, 3714L, 3715L, 3717L, 7814L, 5767L, 7817L, 3723L, 7820L, 7821L, 7823L, 7827L, 7828L, 3733L, 3734L, 5784L, 3737L, 5786L, 3739L, 4321L, 5789L, 6085L, 7840L, 3745L, 7844L, 7497L, 7846L, 7849L, 7850L, 5803L, 7852L, 7853L, 7854L, 1712L, 7857L, 7858L, 3763L, 7860L, 7861L, 7864L, 5818L, 7867L, 5820L, 5821L, 6773L, 3776L, 5825L, 6091L, 3780L, 5830L, 6433L, 7880L, 3787L, 7885L, 7886L, 7888L, 7889L, 7890L, 7891L, 1763L, 7897L, 7898L, 7900L, 7901L, 7902L, 7905L, 5858L, 7907L, 3812L, 7909L, 5863L, 1768L, 7913L, 5867L, 3820L, 2002L, 7919L, 7920L, 7921L, 7922L, 3878L, 3828L, 332L, 2835L, 2719L, 7933L, 7934L, 7936L, 7939L, 7940L, 7944L, 4396L, 1802L, 1806L, 7951L, 3857L, 7955L, 3862L, 7959L, 7960L, 7962L, 7813L, 3872L, 7969L, 7568L, 7974L, 7976L, 7977L, 1671L, 7980L, 7981L, 7982L, 7986L, 3891L, 7988L, 7459L, 1846L, 1847L, 7992L, 436L, 6111L, 5016L, 3901L, 5449L, 5953L, 310L, 6404L, 5959L, 1865L, 5962L, 5965L, 5773L, 8016L, 8017L, 3922L, 3923L, 3925L, 3926L, 4409L, 8024L, 1883L, 3932L, 5981L, 199L, 5983L, 8032L, 5989L, 8039L, 6460L, 3946L, 3949L, 6000L, 6002L, 5779L, 6005L, 5097L, 6009L, 6012L, 6013L, 3966L, 4757L, 6018L, 7830L, 6024L, 1929L, 6026L, 2986L, 1935L, 323L, 4088L, 7833L, 5793L, 4000L, 1008L, 7430L, 7835L, 1957L, 6054L, 4007L, 8019L, 6059L, 4012L, 3816L, 1968L, 6066L, 6131L, 4021L, 6601L, 6135L, 6074L, 6075L, 6077L, 6079L, 1985L, 6084L, 4037L, 6086L, 6087L, 6088L, 6089L, 4043L, 6097L, 6098L, 7502L, 6104L, 6107L, 6109L, 6110L, 4063L, 5659L, 529L, 6116L, 2021L, 5379L, 2026L, 1650L, 6125L, 2030L, 6129L, 4083L, 2036L, 4085L, 2039L, 6136L, 4090L, 5119L, 2044L, 559L, 2047L]
custom_user_ids = [1029L, 1038L, 1039L, 538L, 1054L, 39L, 1069L, 349L, 561L, 564L, 1077L, 569L, 1082L, 1083L, 1084L, 574L, 779L, 1092L, 81L, 596L, 597L, 606L, 1120L, 1125L, 617L, 1132L, 109L, 622L, 112L, 625L, 626L, 1139L, 789L, 133L, 648L, 650L, 1170L, 1171L, 1172L, 1179L, 1180L, 1181L, 671L, 1184L, 1187L, 676L, 1190L, 691L, 1204L, 1209L, 1215L, 1217L, 707L, 1220L, 197L, 712L, 1226L, 1227L, 716L, 211L, 1238L, 1243L, 222L, 1247L, 226L, 1253L, 1254L, 826L, 243L, 762L, 127L, 1276L, 1279L, 768L, 258L, 1284L, 1219L, 1287L, 1290L, 1291L, 1298L, 1301L, 793L, 1306L, 1307L, 285L, 1310L, 1311L, 1312L, 1317L, 49L, 1320L, 1322L, 306L, 1327L, 818L, 1333L, 1336L, 52L, 314L, 1340L, 1342L, 1343L, 1346L, 1347L, 1348L, 1350L, 1351L, 1357L, 849L, 338L, 1363L, 1364L, 342L, 1367L, 1368L, 1369L, 1373L, 865L, 354L, 869L, 876L, 370L, 1086L, 385L, 763L, 394L, 924L, 934L, 424L, 939L, 944L, 945L, 436L, 1183L, 672L, 970L, 461L, 466L, 471L, 985L, 987L, 84L, 993L, 1275L, 1007L, 505L, 1018L, 1019L]
print len(user_ids)
print len(custom_user_ids)
query = (stable.site == "CodeForces") & \
        ((stable.user_id.belongs(user_ids)) | \
         (stable.custom_user_id.belongs(custom_user_ids)))
print "Deleting all the submissions for the given IDs"
print db(query).delete()

print "Resetting codeforces last retrieved for auth_user"
db(atable.id.belongs(user_ids)).update(codeforces_lr=current.INITIAL_DATE)

print "Resetting codeforces last retrieved for custom_friend"
db(cftable.id.belongs(custom_user_ids)).update(codeforces_lr=current.INITIAL_DATE)

print "Resetting delays"
db(nrtable.user_id.belongs(user_ids)).update(codeforces_delay=0)
db(nrtable.custom_user_id.belongs(custom_user_ids)).update(codeforces_delay=0)
