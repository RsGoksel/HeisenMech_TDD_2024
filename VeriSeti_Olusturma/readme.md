  # 2024 Teknofest Doğal Dil İşleme - Serbest Kategori / Otonom Veri Seti Oluşturucu Boru hattı Dokümentasyonu


## Hepsine Hükmedecek Bir Yöntem 💍

İleri düzey bir dil modeli geliştirmek istiyorsanız, güçlü bir veri setine sahip olmanız şarttır. Özellikle Türkçe dil modeli odaklı bir proje üzerinde çalışıyorsanız, veri seti oluşturma süreci büyük önem taşır ve etkili bir yaklaşım gerektirir. Günümüzde bir bilgi veya veri seti talep ettiğinizde, genellikle üç temel kaynağa başvurursunuz: PDF veya DOCX gibi belgeler, web sayfaları ve mevcut JSON veri setleri. <br><br>
Peki, bu kaynakları otonom bir şekilde Türk diline hizmet edecek hale nasıl getirebiliriz? HeisenMech takımı, geliştirdiği otonom boru hattını sunar. 

# Gök-Börü-Hattı

Geliştirdiğimiz otonom sistem, kaynaklardan edindiği tüm bilgileri, API Call ile bir dil modeline bağlar (Projede GROQ üzerinden LLama3 405B modeli kullanıldı). Elde edilen bilgileri, bu dil modeline "Instruction, Reponse, Output" olacak şekilde yeniden yapılandırmasını ister. Yapılandırılmış ve işlenmiş veriler, JSON formatında ve LLM eğitimine uygun formata dönüştürülür ve kaydedilir.

![image](https://github.com/user-attachments/assets/89a2310e-f5dc-4661-8b79-3d7d55d1388c)

Projede en temel 3 bilgi kaynaklarını elde aldık. Bunlar:

* Web sayfaları

*  PDF, DOC, CSV gibi belgeler

*  İnternette mevcut ve veya farklı dillerdeki JSON veri setleri

  # PDF, DOC, CSV türündeki belgeler (DOC2JSON)-> 
  
  * Pdf2Json dosyası ile, dosyaya sadece PDF belgesinin yolu verilir ve boruhattı, tüm pdf'i gezerek (arkaplanda Groq ile 70B Llama dil modeline bağlanarak) bu bilgileri dil modeli eğitim veri setine uygun bir şekilde formatlar.
    
   ![image](https://github.com/user-attachments/assets/97a7bec0-d2a4-4f7f-a136-876e78de3bf3)


# WEB Sayfaları (WEB2JSON)

 * Scraper_Extracter.ipynb dosyası, bir web sitesi linkini alarak ve alt linklerin tümüne ulaşarak tüm textleri elde eder.

# Mevcut JSON Veri Setleri (JSON2JSON)

* JsonEng2JsonTr.ipynb dosyası, mevcut bir json dosyasını alarak ve dil modeline elementleri ayrı ayrı vererek yabancı dildeki bu json veri setini, Türkçe diline uygun hale getirir.
  
(Readme dosyası ve kod dosyaları geliştirme aşamasındadır. Takipte kalın!)
