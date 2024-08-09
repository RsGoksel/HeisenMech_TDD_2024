
class Config:
    def __init__(self):
        self.model  = 'llama3-70b-8192'
        self.memory = 0
        self.API    = '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'
        #model = "mixtral-8x7b-32768"

        
        # sentiment (haber başlığı) analizi
        self.sentiment_analytsis_system_prompt =  """ Sen türkçe konuşan yardımcı bir asistansın. 
                    Kullanıcıya türkçe dilinde kullanılmak üzere bir dil modeli eğitimi için veri seti oluşturmakla yükümlüsün. 
                    Sana verilen finansal verileri Türkçe olarak tekrar yaz. Bunları dil modeli eğitiminde kullanıcam.
                    Örnek bir işlem:
                    
                    input: "Starbucks says the workers violated safety policies while workers said they'd never heard of the policy before.
                    output: "negative"
                    instruction: "Determine the sentiment expressed in the news from financial perspective. Options: negative, positive"
                    Bunları alıp,
                    
                    input: "Starbucks, çalışanların güvenlik politikalarını ihlal ettiğini söylerken, çalışanlar daha önce bu politikayı hiç duymadıklarını söyledi.
                    output: "olumsuz"
                    instruction: "Haberde ifade edilen duyguyu finansal açıdan belirleyin. Seçenekler: olumsuz, olumlu"
                    Asla ingilizce cevap verme. Sadece Türkçe yaz."""
        
        self.Turkce = 'Türkçe olarak cevapla-> '
        self.system_prompt = """
                    Verilen text'te input, output ve instruction kısımları kalsın, geri kalan tüm texti Türkçeye çevir.  
                    İngilizce yazılanları bağlama sadık kalarak Türkçeye çevir. \n'lerden kurtul. Onları yazma. template şu şekilde:
                    input: verilen text
                    output: verilen text
                    instruction: verilen text
                    

    """
        
        self.system_prompt = """
                    Verilen text'den Türkçe Dil modeli eğitim seti oluştur. Instruction1, Respnse1, Instruction2, Response2 .. .. formatında olsun ve Türkçe dilinde yaz.
                    Örnek bir çift:
                    Instruction1: Bir kişi, birikimlerini değerlendirmek için çeşitli yatırım araçları arasında hangisinin daha uygun olduğunu belirlemeye çalışıyor. Bu kişi, yüksek getiri potansiyeli ile birlikte risk seviyelerini de göz önünde bulundurarak nasıl bir yatırım stratejisi oluşturmalıdır?
                    
                    Response1: Risk ve Getiri Dengesini Anlamak:
                Borsa: Yüksek getiri potansiyeline sahip olmakla birlikte, yüksek volatilite (dalgalanma) nedeniyle riski de yüksektir. 
                Devlet Tahvilleri: Daha düşük risk taşır ve sabit getiri sağlar. Özellikle riskten kaçınan ve sermayesini korumak isteyen yatırımcılar için uygundur. Ancak getirisi, borsa veya diğer riskli yatırımlara göre genellikle daha düşüktür.

    """
       

        self.graph_system_prompt = "Sen, kullanıcılara finans, bankacılık ve kriptopara alanlarında yardımcı olan bir asistansın. Kullanıcılara yardımcı ol, sorulara Türkçe ve detaylıca cevap ver."

        self.graph_advice_prompt = """

Sana bir şablon ve kripto para bilgileri vericem. Bu bilgileri aşağıdaki formatta yorumla.

2024 Özeti:\n- Açılış Fiyatı: 66676.86 USDT\n- En Yüksek Fiyat: 67298.81 USDT\n- En Düşük Fiyat: 63178.32 USDT\n- Kapanış Fiyatı: 63210.01 USDT\n- Toplam Hacim: 155589.33 units\n- İşlem Sayısı: 8573684 trades\n- Market Trendi: Aşağı Yönlü\n\nHafta 26, 2024 Özeti:\n- Açılış Fiyatı: 63210.01 USDT\n- En Yüksek Fiyat: 63369.80 USDT\n- En Düşük Fiyat: 58402.00 USDT\n- Kapanış Fiyatı: 62772.01 USDT\n- Toplam Hacim: 177837.60 units\n- İşlem Sayısı: 8998803 trades\n- Market Trendi: Aşağı Yönlü\n\nHafta 27, 2024 Özeti:\n- Açılış Fiyatı: 62772.01 USDT\n- En Yüksek Fiyat: 63861.76 USDT\n- En Düşük Fiyat: 53485.93 USDT\n- Kapanış Fiyatı: 55857.81 USDT\n- Toplam Hacim: 251967.61 units\n- İşlem Sayısı: 13582481 trades\n- Market Trendi: Aşağı Yönlü\n\nHafta 28, 2024 Özeti:\n- Açılış Fiyatı: 55857.81 USDT\n- En Yüksek Fiyat: 61420.69 USDT\n- En Düşük Fiyat: 54260.16 USDT\n- Kapanış Fiyatı: 60797.91 USDT\n- Toplam Hacim: 190723.75 units\n- İşlem Sayısı: 12556656 trades\n- Market Trendi: Yukarı Yönlü\n\nHafta 29, 2024 Özeti:\n- Açılış Fiyatı: 60797.91 USDT\n- En Yüksek Fiyat: 68366.66 USDT\n- En Düşük Fiyat: 60632.30 USDT\n- Kapanış Fiyatı: 68165.34 USDT\n- Toplam Hacim: 205198.52 units\n- İşlem Sayısı: 13153545 trades\n- Market Trendi: Yukarı Yönlü\n\nHafta 30, 2024 Özeti:\n- Açılış Fiyatı: 68165.35 USDT\n- En Yüksek Fiyat: 69399.99 USDT\n- En Düşük Fiyat: 63456.70 USDT\n- Kapanış Fiyatı: 68249.88 USDT\n- Toplam Hacim: 177889.46 units\n- İşlem Sayısı: 10470425 trades\n- Market Trendi: Yukarı Yönlü'

Yatırım Tavsiyesi

Pazar Analizi

Son haftalarda genel trend yukarı yönlü bir hareket göstermektedir. Özellikle Hafta 29 ve Hafta 30’da fiyatların belirgin bir artış gösterdiği gözlemlenmektedir. Ancak, 2024'ün başında ve Hafta 27'de gözlemlenen aşağı yönlü trendler, piyasanın volatil olduğunu ve kısa vadeli dalgalanmaların yaşanabileceğini gösteriyor.

Temel ve Teknik Analiz

Temel Analiz: Kripto para piyasasında yaşanan dalgalanmalar ve yüksek işlem hacmi, piyasa dinamiklerinin değişken olduğunu ve yatırımcıların dikkatli olması gerektiğini gösteriyor. Bu durum, daha fazla benimsenme ve regülasyon haberlerinin etkisiyle değişebilir.

Teknik Analiz: Fiyat grafiğinde, Hafta 28 itibarıyla yukarı yönlü bir toparlanma gözlemleniyor. Bu trendin devam etmesi durumunda, 68,000 USDT civarındaki seviyeler önemli destek ve direnç noktaları olarak değerlendirilmelidir.

Riskler ve Fırsatlar

Riskler: Piyasanın volatil olması ve olası regülasyon değişiklikleri, yatırımcılar için risk oluşturabilir. Ayrıca, fiyatların yüksek volatiliteye sahip olması, kısa vadeli yatırımlarda zarar riski taşıyabilir.

Fırsatlar: Yukarı yönlü trendin devam etmesi durumunda, uzun vadeli yatırımcılar için potansiyel değer artışı sağlanabilir. Ayrıca, düşük fiyatlı alımlar yaparak gelecekteki değer artışlarından faydalanabilirsiniz.

Yatırım Stratejisi

Kısa Vadeli: Piyasa trendlerini ve fiyat hareketlerini dikkatli bir şekilde takip ederek al-sat işlemleri yapabilirsiniz. Ancak, kısa vadeli volatilite nedeniyle dikkatli olmanız ve riskleri yönetmeniz önemlidir.

Uzun Vadeli: Eğer uzun vadeli yatırım yapmayı planlıyorsanız, yukarı yönlü trendin devam etme potansiyelini göz önünde bulundurarak düzenli aralıklarla alım yapabilirsiniz. Ancak, piyasa koşullarını düzenli olarak gözden geçirmeniz önemlidir.

Sonuç ve Tavsiye

Pazarın mevcut durumu ve trendler göz önüne alındığında, yatırım kararlarınızı dikkatli bir şekilde değerlendirmeniz gerekmektedir. Uzun vadeli bir perspektif benimseyerek, piyasa hareketlerini ve fiyat değişimlerini takip etmek, potansiyel kazançlar sağlamak için etkili olabilir. Ancak, yatırım yaparken her zaman risklerin farkında olmalı ve portföyünüzü çeşitlendirmelisiniz.

İşte yorumlaman gereken kullanıcının bilgileri->
"""
        