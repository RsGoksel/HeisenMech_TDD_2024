# Teknofest_NLP
#Acıkhack2024TDDİ

Acıkhack2024TDDİ

![image](https://github.com/user-attachments/assets/706811e9-95de-49ab-8098-2ee73932beb3)

# 2024 Teknofest Doğal Dil İşleme - Serbest Kategori - HeisenMech Takımı Kod Dokümentasyonu

Türkçe Doğal Dil İşleme alanında gerçekleştirdiğimiz çalışmaları Türk Dili ve Türkçe Doğal Dil İşleme Literatürü için açık kaynak olarak paylaşıyoruz. 

## Geliştirdiğimiz Veri Setleri:

* Finansal Sorgular -> https://huggingface.co/datasets/RsGoksel/Teknofest_DS_1
* Duygusal Haber Analizi -> https://huggingface.co/datasets/RsGoksel/Sentiment
* Teknik Finansal Sorular -> https://huggingface.co/datasets/RsGoksel/Finansal

  Tüm veri setlerini, geliştirdiğimiz tam otonom veri seti oluşturucusu ile geliştirdik. Bu boru hattına "Gök-Boru-Hattı" ismini verdik.

  # Otonom Veri Seti Oluşturma - Pipeline
  * Pdf2Json dosyası ile, dosyaya sadece PDF belgesinin yolu verilir ve boruhattı, tüm pdf'i gezerek ve 405B Llama dil modeline bağlanarak bu bilgileri dil modeli eğitim veri setine uygun bir şekilde formatlar.
   ![image](https://github.com/user-attachments/assets/97a7bec0-d2a4-4f7f-a136-876e78de3bf3)

  * Scraper_Extracter.ipynb dosyası, bir web sitesi linkini alarak ve alt linklerin tümüne ulaşarak tüm textleri elde eder.
 
  * JsonEng2JsonTr.ipynb dosyası, mevcut bir json dosyasını alarak ve dil modeline elementleri ayrı ayrı vererek yabancı dildeki bu json veri setini, Türkçe diline uygun hale getirir.

![image](https://github.com/user-attachments/assets/89a2310e-f5dc-4661-8b79-3d7d55d1388c)

   
  # Finansal Asistan - Arayüz

  * app.py dosyası, streamlit kütüphanesi ile çalıştırıldığında finansal asistan arayüzü çalışır
 ![image](https://github.com/user-attachments/assets/f391bdc9-f53a-46de-bb56-52ed0e6c7a6e)
  ```bash
   %cd project_location
    streamlit run app.py
   ```
! App dosyasının çalıştırılması için streamlit kütüphanesinin yüklenmesi gerektiğini hatırlatırız !
     
  * GUI ipynb dosyası ile Binance üzerinden verilen tarihler aralığında veri çekilebilir. (Saatlik, aylık, günlük ve haftalık olarak veri çekilebilmekte)
   ![image](https://github.com/user-attachments/assets/673665d4-8935-40b9-9f85-0bc7579ea3bd)

Çekilen veriler grafik olarak görüntülenebilmekte, detaylı ve sade şekilde olmak üzere bir veri çerçevesi formatında döndürülebilmekte.

  
