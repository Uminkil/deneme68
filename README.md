# Türk İş Hukuku Danışmanlık Botu

Bu proje, Yargıtay kararları ve diğer iş hukuku belgeleri üzerinden Türk İş Hukuku alanında danışmanlık sağlayan bir sohbet botu oluşturmayı amaçlar. Proje, RAG (Retrieval Augmented Generation) mimarisini kullanır.

## Özellikler

- **LLM:** GPT-4 veya Türkçe destekli başka bir model
- **Vektör Veritabanı:** FAISS veya Chroma
- **Dosya Desteği:** PDF formatındaki Yargıtay kararları ve mevzuat dokümanları
- **Arayüz:** Chat tabanlı Streamlit uygulaması
- **İsteğe Bağlı:** Kullanıcı geçmişi saklama, öneri sistemi vb.

## Kurulum

1. Gerekli Python paketlerini kurun:
   ```bash
   pip install -r requirements.txt
   ```
2. PDF dosyalarını `data/` klasörüne yerleştirin.
3. Aşağıdaki komutla uygulamayı çalıştırın:
   ```bash
   streamlit run app.py
   ```
4. Açılan web sayfasında sorularınızı sohbet kutusuna yazıp **Gönder** butonuna basın.

## Klasör Yapısı

```
├── data/                # PDF dosyaları
├── src/                 # Uygulama kodu
├── app.py               # Streamlit arayüzü
├── requirements.txt     # Bağımlılıklar
└── README.md            # Bu dosya
```

## Notlar

Bu depodaki kod başlangıç seviyesindedir ve zamanla geliştirilecektir.
