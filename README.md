# Teknofest_NLP
#Acıkhack2024TDDİ

Acıkhack2024TDDİ
![mech](https://github.com/user-attachments/assets/c48ba4f4-88d8-4455-81b5-cb282e1b9d9b)

# 2024 Teknofest Doğal Dil İşleme - Serbest Kategori - HeisenMech Takımı Kod Dokümentasyonu

Türkçe Doğal Dil İşleme alanında gerçekleştirdiğimiz çalışmaları Türk Dili ve Türkçe Doğal Dil İşleme Literatürü için açık kaynak olarak paylaşıyoruz. 
Projenin sunumuna göz atabilirsiniz ->[ sunum linki](https://www.canva.com/design/DAGLXYyGpM0/fBd43zF1jDLFzCSVUExoZw/edit?utm_content=DAGLXYyGpM0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Takım: HeisenMech
Takım ID: 2290338


# Kazım.. Bize Para Lazım

Günümüz şartlarında finans alanı oldukça değerli ve ülkemiz için hayati bir öneme sahiptir. Ekonomik büyüme ve istikrarın sağlanmasında, yatırımların yönlendirilmesinde ve bireylerin geleceğe yönelik finansal güvenliğinin temin edilmesinde kilit bir rol oynamaktadır. Projemizde bu amaçla "Finansal Okur-yazarlığı Arttırma ve Yatırım Tavsiyesi Asistanı" başlığı altında çalıştık. Geliştirdiğimiz modele "Kazım" ismini verdik. 
Projemimiz sloganı "Kazım, bize para Lazım" :)
________________________________________________________________

https://github.com/user-attachments/assets/c12afd22-1398-4dfa-97b7-c47d6882e193

________________________________________________________________

Geliştirdiğimiz Al-Sat arayüzü, Binance API'si ile "Başlangıç-Bitiş tarihi, Kripto birimi, Aralık" bilgilerini alır, bu verilere göre kripto biriminin değerlerini analiz eder ve teknik analiz sonucunu iletir.
Teknik analiz için modele backend tarafında talep edilen bir şablon verilebilir. Biz Al-Sat tavsiyesi için "Teknik Analiz, Risk Analizi, Sonuç" gibi başlıkları modelden istedik. 

# Model & Veri Seti

## Model

Finans alanında model geliştiriyorsanız oldukça güçlü bir model ve veri setinizin olması gerek. Dil modeli için açık kaynaklı dil modellerinden Meta'nın paylaştığı açık kaynak [Llama3.1](https://llama.meta.com/) mimarisi kullandık. Başlıca Qwen2, Mixtral ve LLama mimarilerinde çalışmalarımız gerçekleştirdik. Bu mimariler için LLama3.1, en uygun formatta ihtiyacımızı karşılayan mimari oldu. Proje dahilinde kullandığımız ve karşılaştırmaları bu belge üzerinde veriyor olacağız. 

## Veri seti

Amacımız doğrultusunda geliştirdiğimiz modelin, hem amatör hem de profesyonel seviyedeki tüm kullanıcılara yardımcı olacak şekilde tasarlanmasıydı. Bu sebeple oldukça çeşitli ve kapsamlı veri setlerine ihtiyaç duyuldu. Buna mukabil yarışmada "Türkçe Doğal Dil İşleme" kapsamına ve Türk literatürüne katkı sağlamak amacıyla muhteşem bir Boruhattı geliştirdik, "Gök-Boru Hattı". Bu sistem sayesinde, "Herhangi" bir konuda dil modeli eğitim seti oluşturabilirsiniz. Tek yapmanız gereken, boru hattına elinizdeki belgeleri sunmak. (Veri seti klasörü altında teknik ve detaylı açıklamalar mevcuttur)

Veri seti oluşturmak için geliştirdiğimiz sistemler tam otonom şekilde çalışmaktadır.  

* Web sayfası: Geliştirmek istediğiniz bir konu ile ilgili web sayfasını sisteme verebilir, websitesindeki tüm alt linklere recursive şeklinde erişip tüm textlerin kullanıldığı bir veri seti elde edebilirsiniz.
  
* PDF & DOCX Belgeleri: Mevcut belgelerinizdeki bilgileri dahi modele eğitim veri seti oluşturmada kullanabilirsiniz. Yine size düşen sadece PDF belgesinin yolunu iletmek

* Mevcut veri setleri: Türkçe olarak veri setine ihtiyacınız var fakat elinizdeki belgeler yabancı dilde mi? Tüm JSOn formatındaki mevcut veri setlerini bu program ile Türkçe'ye bağlama sadık kalcak şekilde çevirebilirsiniz.


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

________________________________________________________

Eğitim seti hazır olan modellerin eğitimi için güçlü bir framework olan UNSLOTH kullanıldı. Unsloth ile dil modelleri PEFT yöntemi ile oldukça hızlı ve düşük maliyette eğitilebilir.    
Colab Notebook Link -> https://colab.research.google.com/drive/10mfw8Yr51JldmdqfbsfABJmTcy0XS6As?usp=sharing
  
