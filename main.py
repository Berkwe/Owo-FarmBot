
import discord, time, random, asyncio, os, json, subprocess
from discord.ext import commands

settingsJs = """{
"Botun_Tokeni": "",
"Oynanacak_Hesabınızın_Tokeni": "",
"Oynanacak_Kanalın_İdsi": "",
"Oynanacak_Sunucunun_idsi": "",
"Komutlara_erişimi_olan_hesabın_idsi": ""
}"""
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, "settings.json")
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(settingsJs)
    raise ValueError("Settings.json dosyası bulunamadığı için bir tane oluşturuldu. Lütfen bilgilerinizi doğru ve EKSİKSİZ şekilde girin.")

with open(file_path, "r", encoding="utf-8") as f:
    settings = json.load(f)

import DiscordClient

# BOT Token
TOKEN = settings["Botun_Tokeni"]
# SELF TOKEN
selfToken = settings["Oynanacak_Hesabınızın_Tokeni"]
# OWO Channel id
channel = int(settings["Oynanacak_Kanalın_İdsi"])
# OWO Server İD
server_id = int(settings["Oynanacak_Sunucunun_idsi"])
# Manager id
manager_id = int(settings["Komutlara_erişimi_olan_hesabın_idsi"])

# Settings #

# Bot prefix
prefix = "-"
# Startup OWO
defaultAmount = 100
amount = defaultAmount
amounts = []
# Captcha protection
captchaProtection = True
# if antiChaptca true,  After how many attempts should it be stopped?
cfLimit = 16
# Dell random messages? (in lst)
dellRandoms = False
# Owo pray bot?
owoPray = True
prayTime = 251
# Limit the spent money
loseTrigger = False
limitValue = 100000
# Randoms list
lst = ["owo battle", "ehue", "hebele", "rastgele", "kelimeler",
        "owo h", "hey", "ahali", "zombi", "mahali", "acılarını"]


# Don't touch
isBotRunning = True
currentlyTime = int(time.time())
isPause = False
isCont = True
won = False
# OWO Bot id
bot_id = 408785106942164992
# İf losing streak
losingStreak = 0
# For cooldown
message_ids = [0, 1]
# For captchaProtection
cfValue = [0, 0]
hebele = False
# For profit calculate
cashControlVal = 0
# Discord settings
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents, )


async def main():
    global won, amount, limitValue, bot_channel, currentlyTime
    if amounts:
        for amount in amounts:
            while isCont and isBotRunning:
                if won == True:
                    amounts.remove(amount)
                    break
               
                if amount*2 > 250000 and isCont:
                    bölü = 2
                    print("LOG : 250000 üstü amount belirlendi, Amounts.amount bölünüyor.")
                    while amount//bölü < 250000:
                            bölü += 1
                            continue
                    for _ in range(bölü):
                        amounts.append(amount//bölü)

                print("\nScattered Amount :", amount)
                await DiscordClient.gönder(message=f"owo cf {amount}", server_id=server_id, channel_id=channel)
                cfValue[1]  += 1
                currentlyTime = int(time.time())
                await asyncio.sleep(1)
                await DiscordClient.gönder(message=random.choice(lst), server_id=server_id, channel_id=channel)
                if isCont:
                    amount *= 2
                await asyncio.sleep(13)
        
    else:
        while isCont and isBotRunning:
            if won == True:
                amount = defaultAmount
                won = False
            
            elif loseTrigger and amount >= limitValue:
            
                await user.send(f"USTA! {limitValue} owo kaybedildi, haberin olsun.")
                amount = defaultAmount

            if amount*2 > 250000 and isCont:
                    bölü = 2
                    print("LOG : 250000 üstü amount belirlendi, amount bölünüyor.")
                    while amount//bölü < 250000:
                            bölü += 1
                            continue
                    for _ in range(bölü):
                        amounts.append(amount//bölü)
    
            print("\nAmount :", amount)
            await DiscordClient.gönder(message=f"owo cf {amount}", server_id=server_id, channel_id=channel)
            cfValue[1]  += 1
            currentlyTime = int(time.time())
            await asyncio.sleep(1)
            await DiscordClient.gönder(message=random.choice(lst), server_id=server_id, channel_id=channel)
            if isCont:
                amount *= 2
            await asyncio.sleep(13)

@bot.event
async def on_disconnect():
    global isCont, main_task, TOKEN

    print('LOG : Bot disconnected. Attempting to reconnect...')
    await asyncio.sleep(5)  
    await bot.close()  
    await asyncio.sleep(2)
    await bot.start(TOKEN) 
    isCont = True
    main_task = asyncio.create_task(main())
    await main_task


@bot.event
async def on_ready():
    global user, bot_channel, main_task
    activity = discord.Activity(
        type=discord.ActivityType.watching, name="Pornhub")
    await bot.change_presence(activity=activity)
    await DiscordClient.ClientLogin(bot)
    user = await bot.fetch_user(manager_id)
    bot_channel = bot.get_channel(channel)
    main_task = asyncio.create_task(main())
    await main_task


async def profit_loss(message):
    global cashControlVal
    embed = discord.Embed(
    title="ㅤㅤ📈**Kar-Zarar Durumu**📈ㅤㅤ",
    description=f"||<@{message.author.id}>||",
    color=discord.Color.gold()
    )
    if cashControlVal > 0:
        embed.add_field(
            name='\u200B',
            value='',
            inline=False
        )
        print(f"\nLOG : Profit-loss : +{cashControlVal}.")
        embed.add_field(
        name='**Durum : **',
        value=f'\n\n* Kar : **+{cashControlVal}**',
        inline=False
        )
    elif cashControlVal < 0:
        embed.add_field(
            name='\u200B',
            value='',
            inline=False
        )
        print(f"\nLOG : Profit-loss : {cashControlVal}.")
        embed.add_field(
        name='**Durum : **',
        value=f'\n\n* Zarar : **{cashControlVal}**',
        inline=False
        )
    else:
        embed.add_field(
            name='\u200B',
            value='',
            inline=False
        )
        print(f"\nLOG : Profit-loss : 0.")
        embed.add_field(
        name='**Durum : **',
        value='\n\n* **Hiç owo kazanıp kaybetmemişsiniz.**',
        inline=False
        )
    await message.channel.send(embed=embed)


@bot.event
async def on_message(message):
    global defaultAmount, isCont, main_task, dellRandoms, cfLimit, captchaProtection, cfValue, prefix ,isPause, isBotRunning
    if int(time.time())-currentlyTime > 15 and cfValue[1]-cfValue[0] > 1:
        isBotRunning = False
        isPause = True
    if message.author.id == bot_id and message.channel.id == channel:
        if "Slow down" in message.content and not hebele and int(message.content.replace("_", "").replace("*", "").replace(",", "").replace(">", "").replace("<", "").replace("R", "").replace("t", "").replace(":", "").split()[10]) < (int(time.time())+20):
            print("\nLOG : Cooldown...")
            isPause = True
            main_task.cancel()
            isCont = False
            while True:
                try:
                    await bot_channel.fetch_message(message.id)
                except discord.errors.NotFound:
                    break
            await DiscordClient.sil(message_ids[0], server_id=server_id, channel_id=channel)
            await DiscordClient.sil(message_ids[1], server_id=server_id, channel_id=channel)
            isPause = False
            isCont = True
            main_task = asyncio.create_task(main())
            await main_task

        elif "complete your captcha" in message.content:
            print("\nLOG : Captcha detected, Program suspended...")
            isCont = False
            main_task.cancel()
            await user.send("Captcha tespit edildi, lütfen captchayı tamamlayın.")

    if message.author == bot.user:
        return

    elif message.author.id == manager_id and message.channel.id == channel:
        if message.content.startswith("owo cf "):
            message_ids[0] = message.id

        elif message.content in lst:

            if dellRandoms:
                await DiscordClient.sil(message.id, server_id=server_id, channel_id=channel)

            else:
                message_ids[1] = message.id

        elif message.content == f"{prefix}komutlar" or message.content == f"{prefix}yardım" or message.content == f"{prefix}help":
            embed = discord.Embed(
                title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🤖 OwO Farm Bot 🤖"+"\n\n📜 Yardım Menüsü",
                description="**Botun kullanılabilir komutları aşağıda listelenmiştir :** ",
                color=discord.Color.gold()
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
        
            embed.add_field(
                name=f"🔧 {prefix}randoms aç/kapa",
                value="* **Random mesajları açar veya kapatır. (default=kapalı)**",
                inline=False
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
            embed.add_field(
                name=f"⏸️ {prefix}durdur",
                value="* **Botu dondurur.**",
                inline=False
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
            embed.add_field(
                name=f"▶️ {prefix}başlat",
                value="* **Botu devam ettirir.**",
                inline=False
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
            embed.add_field(
                name=f"🔒 {prefix}captchaprotect aç/kapa/cf_limit",
                value="* **Captcha korumasını açar, kapatır veya mesaj limitini ayarlar. (default=açık)**",
                inline=False
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
            embed.add_field(
                name=f"🍀 {prefix}pray aç/kapa",
                value="* **Botun otomatik olarak owo pray almasını sağlar. (default=açık)**",
                inline=False
            )
            embed.add_field(
                name=f"💰 {prefix}miktar başlangıç_miktarı",
                value="* **Başlangıç miktarını gösterir veya değiştirir.**",
                inline=False
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
            embed.add_field(
                name=f"📈 {prefix}kar-zarar",
                value="* **Başlangıçtan baz alarak kar-zarar durumunu gösterir.(Çok fazla gösterebiliyor.)**",
                inline=False
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
            embed.add_field(
                name=f"🔤 {prefix}prefix ayarlanacak_prefix",
                value="* **Botun geçerli prefix'ini değiştirir.**",
                inline=False
            )
            embed.add_field(
                name='\u200B',
                value='',
                inline=False
            )
            embed.add_field(
                name=f"❓ {prefix}yardım/komutlar/help",
                value="* **Yardım menüsünü gösterir.**",
                inline=False
            )
        
            embed.set_footer(
                text="-# Coded by berkwe_",
            )
        

            await message.channel.send(embed=embed)
        elif message.content.startswith(f"{prefix}pray"):

            if len(message.content.split()) == 2:

                if message.content.split()[1] == "aç":
                    if owoPray:
                        await message.channel.send(f"<@{message.author.id}> **Oto Pray** zaten açık!")

                    else:
                        owoPray = True
                        await message.channel.send(f"<@{message.author.id}> **Oto Pray** açıldı!")

                elif message.content.split()[1] == "kapa" or message.conten.split()[1] == "kapat":

                    if not owoPray:
                        await message.channel.send(f"<@{message.author.id}> **Oto Pray** zaten kapalı!")

                    else:
                        owoPray = False
                        await message.channel.send(f"<@{message.author.id}> **Oto Pray** kapatıldı!")

                else:
                    await message.channel.send(f"<@{message.author.id}> Lütfen sadece aç/kapa kullanın!")

            else:
                await message.channel.send(f"<@{message.author.id}> Bu komut şu şekilde kullanılmalıdır : {prefix}pray aç/kapa")

        elif message.content.startswith(f"{prefix}prefix"):

            if len(message.content.split()) == 2:

                if message.content.split()[1] == prefix:
                    await message.channel.send(f"<@{message.author.id}> Prefix zaten {prefix}")

                else:
                    try:
                        int(message.content.split()[1])
                        await message.channel.send(f"<@{message.author.id}> Prefix'i sayı olarak ayarlayamazsın!")
                    except ValueError:
                        prefix = message.content.split()[1]
                        await message.channel.send(f"<@{message.author.id}> Prefix {prefix} olarak ayarlandı!")
                
            else:
                await message.channel.send(f"<@{message.author.id}> Komut şöyle kullanılmalıdır : {prefix}randoms ayarlanacak_prefix")

        elif message.content == f"{prefix}kar-zarar":
            await profit_loss(message)
        

        elif message.content.startswith(f"{prefix}randoms"):
            if len(message.content.split()) == 2:

                if message.content.split()[1] == "aç":

                    if not dellRandoms:
                        await message.channel.send(f"<@{message.author.id}> Randoms zaten açık.")

                    else:
                        dellRandoms = False
                        await message.channel.send(f"<@{message.author.id}> Artık random mesajlar silinmeyecek")
                        print("\nLOG : DellRandoms kapatıldı.")

                elif message.content.split()[1] == "kapa":
                    if dellRandoms:
                        await message.channel.send(f"<@{message.author.id}> Randoms zaten kapalı.")
                    else:
                        dellRandoms = True
                        await message.channel.send(f"<@{message.author.id}> Artık random mesajlar silinecek.")
                        print("\nLOG : DellRandoms açıldı.")

                else:
                    await message.channel.send(f"<@{message.author.id}> Lütfen sadece aç veya kapa girin.")

            else:
                await message.channel.send(f"<@{message.author.id}> Komut şöyle kullanılmalıdır : {prefix}randoms aç/kapa")

        elif message.content == f"{prefix}durdur":
            main_task.cancel()
            isCont = False
            isPause = True
            await message.channel.send(f"<@{message.author.id}> Bot başarıyla durduruldu!")
            print("\nLOG : Bot durduruldu.")

        elif message.content == f"{prefix}başlat":
            isCont = True
            isPause = False
            await message.channel.send(f"<@{message.author.id}> Bot başarıyla başlatıldı!")
            main_task = asyncio.create_task(main())
            await main_task

        elif message.content.startswith(f"{prefix}captchaprotect"):

            if len(message.content.split()) == 2:

                if message.content.split()[1] == "aç":

                    if captchaProtection:
                        await message.channel.send(f"<@{message.author.id}> captcha Protection zaten açık.")

                    else:
                        cfValue[1] = 1
                        cfValue[0] = 1
                        captchaProtection = True
                        await message.channel.send(f"<@{message.author.id}> Artık her **{cfLimit}** mesajda bot 3 dakika bekleyecek.")
                        print("\nLOG : captcha Protection açıldı.")

                elif message.content.split()[1] == "kapa" or message.content.split()[1] == "kapat":

                    if not captchaProtection:
                        await message.channel.send(f"<@{message.author.id}> Captcha Protection zaten kapalı.")

                    else:
                        captchaProtection = False
                        await message.channel.send(f"<@{message.author.id}> Artık Captcha protection kapalı.")
                        print("\nLOG : Captcha protection kapandı.")

                else:
                    try:
                        cfLimit = int(message.content.split()[1])
                        if cfLimit > 4:
                            await message.channel.send(f"<@{message.author.id}> Mesaj limiti **{cfLimit}** olarak ayarlandı.")
                            cfValue[1] = 1
                            cfValue[0] = 1
                        else:
                            cfLimit = 30
                            await message.channel.send(f"<@{message.author.id}> Mesaj limiti en az 5 olmalıdır.")
                    except ValueError:
                        await message.channel.send(f"<@{message.author.id}> Lütfen sadece aç veya kapa girin, mesaj limitini değiştirmek isterseniz sayı girin.")
                    
            else:
                await message.channel.send(f"<@{message.author.id}> Komut şöyle kullanılmalıdır : {prefix}captchaprotect aç/kapa/cf_limit")

        elif message.content.startswith(f"{prefix}miktar"):

            if len(message.content.split()) == 1:
                await message.channel.send(f"<@{message.author.id}> Şuanki başlangıç miktarı : {defaultAmount}")

            elif len(message.content.split()) == 2:
                try:
                    defaultAmount = int(message.content[7:])
                    await message.channel.send(f"<@{message.author.id}> Başlangıç miktarı başarıyla değiştirildi!")
                    print("LOG : Başlangıç miktarı değiştirildi.")

                except ValueError:
                    await message.channel.send(f"<@{message.author.id}> Lütfen bir sayı girin!")

            else:
                await message.channel.send(f"<@{message.author.id}> Komut şöyle kullanılmalıdır : {prefix}miktar başlangıç_miktarı")




@bot.event
async def on_message_edit(before, after):
    global won, isCont, losingStreak, main_task, hebele, cfValue, amount, isPause, cashControlVal, owoPray, prayTime
    if after.author.id == bot_id and after.channel.id == channel:

        if "you won" in after.content:
            won = True
            cashControlVal += (amount//2) if cashControlVal != 0 else defaultAmount
            losingStreak = 0
            print(f"\nLOG : KAZANILDI, {defaultAmount}")
            cfValue[0] += 1
            
            
            if captchaProtection and cfValue[0] >= cfLimit:
                cfValue[1] = 1
                cfValue[0] = 1
                messsages = await after.channel.send(f"<@{manager_id}> Captcha koruması için 4 dakika beklenecek. Bot, **<t:{int(time.time())+240}:R>** aktive olacak.")
                print("\nLOG : Waiting 3 min for captchaProtection.")
                hebele = True
                isCont = False
                main_task.cancel()

                await asyncio.sleep(240)
                await messsages.delete()
                hebele = False
                if not isPause:
                    isCont = True
                    main_task = asyncio.create_task(main())
                    await main_task

        elif "you lost" in after.content:
            cashControlVal -= defaultAmount if losingStreak == 0 else amount//2
            print(cashControlVal)
            losingStreak += 1
            print(f"\nLOG : KAYBEDİLDİ")
            cfValue[0] += 1

            if losingStreak == 5:
                isCont = False
                main_task.cancel()
                
                losingStreak = 0
                print("\nLOG : Losing streak, sleeping 45 seconds...")
                message = await after.channel.send(f"Kaybetme serisi 5'e ulaştı, program  **<t:{int(time.time())+46}:R>** çalışacak. Bir sonraki miktar : {amount}")
                await asyncio.sleep(45)
                await message.delete()
                if not isPause:
                    isCont = True
                    main_task = asyncio.create_task(main())
                    await main_task

    if owoPray and int(time.time())-prayTime > 250:
        await DiscordClient.gönder(message="owo pray", server_id=server_id, channel_id=channel)
        prayTime = int(time.time())

    

if __name__ == "__main__":
    bot.run(TOKEN)