# Molekit — Gizlilik Politikası ve Kullanım Koşulları

Tek sayfa, 6 dil (en, tr, de, es, fr, pt-BR). Dil `?lang=xx` ile seçilir; yoksa tarayıcı diline göre açılır.

- Metinler: `src/<dil>.html` (İngilizce ana metin `src/en.html`). Değiştirdikten sonra: `python3 legal/build.py`
- Yayın: `.github/workflows/legal-pages.yml`, `main`'e `legal/` değişikliği gelince GitHub Pages'e yükler
  (bir kez: repo → Settings → Pages → Source: **GitHub Actions**).

Adresler (yayınlandıktan sonra):

| Ne | Adres |
|---|---|
| Gizlilik politikası (App Store "Privacy Policy URL") | https://behrank.github.io/Molekit/privacy.html |
| Kullanım koşulları | https://behrank.github.io/Molekit/terms.html |
| İletişim / destek (App Store "Support URL") | https://behrank.github.io/Molekit/contact.html |
| Belirli dil | sonuna `?lang=de` ekle, ör. `privacy.html?lang=de` |
