#Acıkhack2024TDDİ
Acıkhack2024TDDİ

<div style="text-align: right;">

![mech](https://github.com/user-attachments/assets/c48ba4f4-88d8-4455-81b5-cb282e1b9d9b)
![TEKNOFEST](https://img.shields.io/badge/TEKNOFEST-blue)
![Bilişim Vadisi](https://img.shields.io/badge/B%C4%B0L%C4%B0%C5%9E%C4%B0M%20VAD%C4%B0S%C4%B0-cyan)
![Açık Kaynak TR](https://img.shields.io/badge/A%C3%A7%C4%B1k%20Kaynak%20TR-green)
![HeisenMech](https://img.shields.io/badge/HeisenMech-purple)
</div>

# 2024 Teknofest Doğal Dil İşleme - Serbest Kategori - HeisenMech Takımı Kod Dokümentasyonu

Türkçe Doğal Dil İşleme alanında gerçekleştirdiğimiz çalışmaları Türk Dili ve Türkçe Doğal Dil İşleme Literatürü için açık kaynak olarak paylaşıyoruz. 
Projenin sunumuna göz atabilirsiniz ->[Sunum linki](https://www.canva.com/design/DAGLXYyGpM0/fBd43zF1jDLFzCSVUExoZw/edit?utm_content=DAGLXYyGpM0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Takım: HeisenMech
Takım ID: 2290338


# Kazım.. Bize Para Lazım

Günümüz şartlarında finans alanı oldukça değerli ve ülkemiz için hayati bir öneme sahiptir. Ekonomik büyüme ve istikrarın sağlanmasında, yatırımların yönlendirilmesinde ve bireylerin geleceğe yönelik finansal güvenliğinin temin edilmesinde kilit bir rol oynamaktadır. Projemizde bu amaçla "Finansal Okur-yazarlığı Arttırma ve Yatırım Tavsiyesi Asistanı" başlığı altında çalıştık. Geliştirdiğimiz modele "Kazım" ismini verdik. 
Projemimiz sloganı "Kazım, bize para Lazım" :)

Projemizin arayüzlerinden biri olan, "Yatırım tavsiyesi & Teknik Analiz" işlemleri için geliştirdiğimiz arayüz 
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

________________________________________________________

Eğitim seti hazır olan modellerin eğitimi için güçlü bir framework olan UNSLOTH kullanıldı. Unsloth ile dil modelleri PEFT yöntemi ile oldukça hızlı ve düşük maliyette eğitilebilir.    
Colab Notebook Link ->  [![Colab](https://img.shields.io/static/v1?label=Demo&message=Colab&color=orange)](https://colab.research.google.com/drive/10mfw8Yr51JldmdqfbsfABJmTcy0XS6As?usp=sharing)

