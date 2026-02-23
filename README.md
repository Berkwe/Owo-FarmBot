# ⚠️ FİXLENMİŞ/DESTEĞİ KESİLMİŞTİR
# 🤖 OwO Farm Bot 🤖

## 📜 Açıklama

Bu proje, Discord üzerindeki OWO botunda otomatik OWO kasmak için yapılmıştır. Bot, belirtilen sunucuda otomatik olarak coinflip oynayarak, belirli bir para miktarı ile başlar. Para miktarı her kaybedildiğinde ikiye katlanır ve doğru miktar girildiğinde matematiksel olarak 0.5 kaybetme olasılığı ile para kasar. Ayrıca çeşitli koruma ve yönetim işlevlerine de sahiptir.
**[Sıkıcı yerleri geç](https://github.com/Berkwe/Owo-SelfBot#kurulum-ad%C4%B1mlar%C4%B1)(lütfen geçme :3)**

## 🚀 Özellikler
- **Tamamen requestler üzerinde yapıldığından, python çalıştıran herhangi bir makinada(termux, kali, windows cmd vb.) kullanılabilmekterdir.**
- **Otomatik İşlem:** Başlangıç miktarı ile `owo cf` komutunu gönderir ve işlemleri otomatik olarak yürütür.
- **Captcha Koruması:** Captcha tespit edildiğinde botu geçici olarak durdurur ve kullanıcıyı bilgilendirir.
- **Otomatik Pray:** Eğer istenirse her 5 dakikada bir `owo pray` komutunu gönderir.
- **Bekleme yok!:** 12 saniyelik sürede cooldowna düşerseniz bunu anlar ve cooldown bitişinde aynı miktar ile yeniden oynar..
- **Komutlar:** Botun çeşitli işlevlerini kontrol eden komutlar sağlar.

## ⚠️ NOT
 - **Bu botun kullanımından oluşabilecek tüm sorumluluk kullanıcıya aittir. Ayrıca test aşamasındadır, eğer bir hata tespit ederseniz lütfen github veya iletişim kısmından iletin.**
 - **Botun kaynak kodu düzenli değildir, başta son kullanıcı hedeflenmediğinden sadece kendimin anlayabileceği şekilde yazmıştım. Kaynak kodu karışık olabilir.**
 - **Botu kullanmak için ayrıca farklı bir discord botu oluşturmanız gerekecek. Neyseki bu çok basit! [Şuradan](https://youtu.be/xc_0Mv11FLA?si=WuLxgIEpuTohV5nY) bir youtube videosuna ulaşabilirsiniz.**

## 🛠️ Kurulum


## 💾 Exe Şeklinde

- **+** Gereksinim yok
- **+** Kurulum yok
- **-** Kaynak kodu düzenlenemez
- **-** Smart screen hatası.
  
## Smart screen hatası nedir?
- **Smart Screen, kötü amaçlı yazılımları ve phishing (oltalama) sitelerini tanımlamaya yardımcı olan bir güvenlik teknolojisidir. Bu sistem, kullanıcıların güvenliğini artırmak için çeşitli yöntemler kullanır.**

## Uygulamanız neden smart screene takılıyor virüslümü?
- **Hayır, alakası yok. Smart screen bir programı tanırken sunucularında kayıtlı lisansları kontrol eder. Eğer uygulamanın lisansı kayıtlı değilse, bir hata mesajı gösterir. Bizimde Lisans alamamızın tek nedeni bunun paralı olması.**
- **Ayrıca, her smart screen hatası aynı değildir. Smart screen mavi arka planlı bir hata verdiğinde uygulamanın tanınmadığını (lisansı bulunmadığını), kırmızı arka planlı bir mesaj verdiğinde uygulamanın virüslü olduğunu belirtir.**

## Smart screen hatasını nasıl geçerim?
1. <img src="https://github.com/user-attachments/assets/0fb7ce67-d366-4393-ac74-f0a3e8106fee" alt="Açıklama" width="300" height="200">
2. <img src="https://github.com/user-attachments/assets/be013ed4-6ffe-440a-b93a-8141e01269ef" alt="Açıklama" width="300" height="200">

## Virüs totalde neden virüs olarak gösteriyor?
- **Uygulamada aynı şekilde Lisans olmadığından dolayı öyle gösteriyor. Test amaçlı sizde `pyinstaller` kütüphanesini kullanarak, içi boş bile olsa python kodunuzu exeye çevirdiğinizde; virüs total virüslü olarak gösterecekdir.**


## Kurulum Adımları
1. **Exe'yi indirin:**
   [OwO Farm-Bot.exe](https://github.com/Berkwe/Owo-FarmBot/releases/latest/download/OwO.Farm-Bot.exe)
3. **Herhangi bir klasöre aktarın.**
4. **Çift tıklayıp çalıştırın. Bot, sizin için settings.json adında ayarlar dosyası oluşturacak.**
5. **Ayarları yapılandırın, [Yapılandırma](https://github.com/Berkwe/Owo-SelfBot#ayarlar)**
6. **Hazırsınız. Programı çalıştırıp discord üzerinden komutlarla kontrol edebilirsiniz.**

## 🐍 Python Şeklinde:

### Gereksinimler

- Python 3.6 veya üzeri

## Kurulum Adımları

1. ### Projeyi indirme:

   - **[Zip](https://github.com/Berkwe/Owo-SelfBot/archive/refs/heads/main.zip)'i indirin**
     ### **Veya**
   - **Git ile klonlayın:**
   ```bash
   git clone https://github.com/Berkwe/Owo-SelfBot
   cd Owo-SelfBot
   ```
2. ### Kurulum:
  **Gerekli modülleri yükleyin:**
   ```bash
   python -r requirements.txt
   ```
3. ### Ayarlar:
   - **`settings.json` dosyasını içini bilgilerinizle EKSİKSİZ biçimde doldurun:**
     ```json
     {
       "Botun_Tokeni": "YOUR_BOT_TOKEN", 
       "Oynanacak_Hesabınızın_Tokeni": "YOUR_SELF_TOKEN",
       "Oynanacak_Kanalın_İdsi": "YOUR_CHANNEL_ID",
       "Oynanacak_Sunucunun_idsi": "YOUR_SERVER_ID",
       "Komutlara_erişimi_olan_hesabın_idsi": "YOUR_MANAGER_ID"
     }
     ```
   - **Örnek doldurma:**
     ```json
     {
       "Oluşturduğunuz_discord_Botunun_Tokeni": "yJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRyLVRSIiwiYnJvd3Nlcl91", 
       "Oynanacak_Hesabınızın_Tokeni": "yJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRyLVRSIiwiYnJvd3Nlcl91",
       "Oynanacak_Kanalın_İdsi": "1145599685621461093",
       "Oynanacak_Sunucunun_idsi": "807266252191170561",
       "Komutlara_erişimi_olan_hesabın_idsi": "461206901040873483"
     }
     ```
     
## 📜 Komutlar
- **Komutlar discord üzerinden botun oynanıdğı kanalda, Manager id ile belirtilen kullanıcı tarafından kullanılabilir.**
- `-randoms aç/kapa` - Random mesajları açar veya kapatır.
- `-durdur` - Botu dondurur.
- `-başlat` - Botu devam ettirir.
- `-captchaprotect aç/kapa/cf_limit` - Captcha korumasını açar, kapatır veya mesaj limitini ayarlar.
- `-pray aç/kapa` - Otomatik pray özelliğini açar veya kapatır.
- `-miktar başlangıç_miktarı` - Başlangıç miktarını gösterir veya değiştirir.
- `-kar-zarar` - Kar-zarar durumunu gösterir.
- `-prefix ayarlanacak_prefix` - Botun geçerli prefix'ini değiştirir.
- `-yardım` - Yardım menüsünü gösterir.

## ⚙️ Kullanım

1. **Botu Başlatma:**
   - Ayarları hallettiyseniz, Botu başlatmak için terminalde şu komutu çalıştırın:
     ```bash
     python bot.py
     ```

2. **Botun Yönetimi:**
   - Botu yönetmek için, belirtilen komutları kullanarak çeşitli ayarları ve işlevleri kontrol edebilirsiniz.

## 📝 Öneriler ve Notlar
- `DiscordClient.py` modülünün, discord kuralları gereğince direkt olarak kaynak kodu sunulmamıştır. Lütfen kurcalamayınız, Geliştirmek isterseniz `main.py`'yi geliştirebilirsiniz.
- Botun başarılı bir şekilde çalışabilmesi için `settings.json` dosyasındaki bilgilerin doğru bir şekilde doldurulması gerekmektedir.
- Botun düzgün çalışması için [Developer portaldan](https://discord.com/developers/applications) oluşturduğunuz botun sunucuda olup ayarlarda belirttiğiniz kanala erişebilmesi gerekmektedir.
- Botun düzgün çalışması için özel bir kanal açmanız ŞİDDETLE tavsiye edilir. Farklı kullanıcıların erişebileceği kanallar botu şaşırtabilir.
- Bot her seferinde 2x katladığı için 5. katlamada paranız yüzbinlere ulaşabilir. Giriş değerini düşük tutmaya çalışın ve owo botunun hileli olduğunu unutmayın. TÜM PARANIZI KAYBEDEBİLİRSİNİZ!!!!!
- Captcha koruma özelliği aktif olduğunda, bot captcha doğrulamasını bekleyecektir. 3 kere captchayı dmden sordukdan sonra, OWO botu artık site üzerinden doğrulama yapacaktır. captcha korumasını kapatmayın ve süresini mümkün olduğunca uzun tutun.

## 📞 İletişim

<a href="https://discord.gg/Xagnh5aYSy" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="F7qaRp22bW" height="30" width="40" /></a>

---

## 📝 Lisans

Bu proje [GPL Lisansı](https://github.com/Berkwe/Owo-SelfBot?tab=GPL-3.0-1-ov-file#) altında lisanslanmıştır.
