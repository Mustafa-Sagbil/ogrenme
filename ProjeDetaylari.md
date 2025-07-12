# PROJE DETAYLARI
# Mustafa'nın Öğrenme Yolculuğu - Proje Açıklamaları

## KULLANIM KILAVUZU
- Bu dosya proje açıklamalarını içerir
- Çözüm yaklaşımları için `CozumYaklasimlari.md` dosyasına bakın
- Her proje için problem tanımı, girdi/çıktı formatları ve öğrenme hedefleri bulunur

---

## 1. PYTHON ÖĞRENME YOLU

### Seviye 1: Temel Kavramlar ve İlk Problemler

#### 1.1. Merhaba Dünya (print, tkinter)

**Problem Tanımı:**
Python'da temel çıktı fonksiyonlarını kullanarak konsola "Merhaba Dünya" yazdırma ve basit bir grafik arayüzü (tkinter ile) kullanarak aynı mesajı bir pencerede gösterme.

**Girdi Formatı:**
- Kullanıcı girdisi yok

**Beklenen Çıktı:**
- Konsol: "Merhaba Dünya"
- GUI Penceresi: "Merhaba Dünya" mesajı

**Şartlar:**
- print() fonksiyonu kullanılmalı
- tkinter kütüphanesi kullanılmalı
- Basit bir pencere oluşturulmalı
- PEP 8 standartlarına uygun olmalı

**Öğrenme Hedefleri:**
- print() fonksiyonu kullanımı
- tkinter kütüphanesi ile GUI
- Temel Python syntax
- Konsol ve GUI farkları

---

#### 1.2. Basit Hesap Makinesi

**Problem Tanımı:**
Kullanıcıdan matematiksel ifadeler alarak temel aritmetik işlemleri (toplama, çıkarma, çarpma, bölme) yapabilen ve olası hataları (sayı olmayan girdi gibi) yönetebilen bir komut satırı uygulaması.

**Girdi Formatı:**
- İlk sayı: 10
- Operatör: +, -, *, /
- İkinci sayı: 5

**Beklenen Çıktı:**
- "10 + 5 = 15"
- Hata durumunda: "Geçersiz girdi!"

**Şartlar:**
- 4 temel işlem desteklenmeli
- Sıfıra bölme kontrolü yapılmalı
- Geçersiz girdi kontrolü yapılmalı
- Sürekli çalışan döngü olmalı
- PEP 8 standartlarına uygun olmalı

**Öğrenme Hedefleri:**
- input() fonksiyonu
- try/except hata yönetimi
- while döngüsü
- if/elif/else koşulları
- Temel matematik operatörleri

---

#### 1.3. İki Sayının Toplamı (Algoritma)

**Problem Tanımı:**
Verilen bir dizide, toplamı belirli bir hedef sayıya eşit olan iki sayıyı bul.

**Girdi Formatı:**
- `nums`: [2, 7, 11, 15] (sayı dizisi)
- `target`: 9 (hedef toplam)

**Beklenen Çıktı:**
- `[0, 1]` (nums[0] + nums[1] = 2 + 7 = 9)

**Şartlar:**
- Tam olarak bir çözüm var
- Aynı elemanı iki kez kullanamazsın
- Dizi sıralı değil
- Time complexity: O(n)
- Space complexity: O(n)
- PEP 8 standartlarına uygun olmalı

**Öğrenme Hedefleri:**
- Hash Table kullanımı
- Time/Space complexity analizi
- Array traversal teknikleri
- Dictionary/Map veri yapısı

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 1.4. Sayı Tahmin Oyunu

**Problem Tanımı:**
Bilgisayarın rastgele seçtiği bir sayıyı kullanıcının tahmin etmeye çalıştığı, kullanıcının girdilerine göre ipuçları veren ve doğru tahmin edene kadar devam eden interaktif bir oyun.

**Girdi Formatı:**
- Kullanıcı tahmini: 50
- Bilgisayar cevabı: "Daha büyük bir sayı girin"

**Beklenen Çıktı:**
- İpucu mesajları
- Doğru tahmin: "Tebrikler! Sayıyı buldunuz."

**Şartlar:**
- 1-100 arası rastgele sayı
- Kullanıcıya ipuçları verilmeli
- Kaç denemede bulduğu sayılmalı
- Oyun tekrar oynanabilmeli
- PEP 8 standartlarına uygun olmalı

**Öğrenme Hedefleri:**
- random modülü
- while döngüleri
- Kullanıcı etkileşimi
- Koşullu ifadeler
- Oyun döngüsü mantığı

---

#### 1.5. Palindrom Kontrolü (Algoritma)

**Problem Tanımı:**
Verilen bir dizenin palindrom olup olmadığını kontrol etme (hem tersten hem düzden okunduğunda aynı olan kelime/cümle).

**Girdi Formatı:**
- `s`: "racecar" veya "A man a plan a canal Panama"

**Beklenen Çıktı:**
- `True` (palindrom ise)
- `False` (palindrom değilse)

**Şartlar:**
- Büyük/küçük harf duyarsız
- Boşluklar ve noktalama işaretleri yok sayılmalı
- Time complexity: O(n)
- Space complexity: O(1) (in-place)
- PEP 8 standartlarına uygun olmalı

**Öğrenme Hedefleri:**
- String manipulation
- Two pointer tekniği
- Character filtreleme
- In-place algoritma

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 1.6. Basit Quiz Uygulaması

**Problem Tanımı:**
Kullanıcıya önceden tanımlanmış sorular soran, cevaplarını alıp doğrulayan, puan hesaplayan ve sonuçları bir dosyaya kaydedip okuyabilen basit bir bilgi yarışması uygulaması.

**Girdi Formatı:**
- Soru: "Türkiye'nin başkenti neresidir?"
- Kullanıcı cevabı: "Ankara"

**Beklenen Çıktı:**
- Doğru/yanlış mesajları
- Toplam puan
- Sonuç dosyası

**Şartlar:**
- En az 5 soru olmalı
- Puan sistemi olmalı
- Sonuçlar dosyaya kaydedilmeli
- Quiz geçmişi okunabilmeli
- PEP 8 standartlarına uygun olmalı

**Öğrenme Hedefleri:**
- Liste ve sözlük kullanımı
- Dosya okuma/yazma
- Puan hesaplama
- Veri yapıları

---

#### 1.7. Faktöriyel Hesaplama (Algoritma)

**Problem Tanımı:**
Verilen bir sayının faktöriyelini hesaplama.

**Girdi Formatı:**
- `n`: 5

**Beklenen Çıktı:**
- `120` (5! = 5 × 4 × 3 × 2 × 1 = 120)

**Şartlar:**
- Recursion ve iteration yöntemleri
- Big number handling (büyük sayılar için)
- Time complexity analizi
- Edge case: 0! = 1
- PEP 8 standartlarına uygun olmalı

**Öğrenme Hedefleri:**
- Recursion kavramı
- Iteration vs recursion
- Big number handling
- Time complexity analizi

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 1.8. Fibonacci Dizisi (Algoritma)

**Problem Tanımı:**
Fibonacci dizisinin n. terimini hesaplama.

**Girdi Formatı:**
- `n`: 10

**Beklenen Çıktı:**
- `55` (10. Fibonacci sayısı)

**Şartlar:**
- Recursion vs iteration
- Dynamic programming giriş
- Time complexity: O(n)
- Space complexity: O(1)

**Öğrenme Hedefleri:**
- Recursion vs iteration
- Dynamic programming
- Memory optimization
- Sequence generation

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

### Seviye 2: Veri Yapıları ve Orta Seviye Algoritmalar

#### 2.1. Kişi Rehberi

**Problem Tanımı:**
Kişilerin ad, soyad, telefon gibi bilgilerini saklayabilen, yeni kişi ekleme, mevcut kişiyi düzenleme, silme ve arama gibi temel CRUD operasyonlarını JSON dosyası kullanarak yönetebilen bir uygulama.

**Girdi Formatı:**
- Ad: "Ahmet"
- Soyad: "Yılmaz"
- Telefon: "0555-123-4567"

**Beklenen Çıktı:**
- Kişi listesi
- Arama sonuçları
- JSON dosyası

**Şartlar:**
- CRUD operasyonları (Create, Read, Update, Delete)
- JSON dosya işlemleri
- Arama fonksiyonu
- Veri kalıcılığı

**Öğrenme Hedefleri:**
- OOP prensipleri
- JSON formatı
- CRUD operasyonları
- Dosya işlemleri

---

#### 2.2. En Uzun Ortak Önek (Algoritma)

**Problem Tanımı:**
Bir dizi dize içinde en uzun ortak öneki bulma.

**Girdi Formatı:**
- `strs`: ["flower", "flow", "flight"]

**Beklenen Çıktı:**
- `"fl"` (en uzun ortak önek)

**Şartlar:**
- En az 1 dize olmalı
- Boş dize durumu kontrol edilmeli
- Time complexity: O(S) (S = tüm dizelerin toplam uzunluğu)

**Öğrenme Hedefleri:**
- String manipulation
- Prefix Tree (Trie) kavramı
- Array traversal
- Edge case handling

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 2.3. Basit Banka Hesabı

**Problem Tanımı:**
Farklı hesap türleri (örneğin vadesiz, vadeli) için kalıtım kullanarak nesne tabanlı bir bankacılık sistemi simülasyonu oluşturma.

**Girdi Formatı:**
- Hesap türü: "Vadesiz" veya "Vadeli"
- İşlem türü: "Para Yatır" veya "Para Çek"
- Miktar: 1000

**Beklenen Çıktı:**
- Bakiye bilgisi
- İşlem onayı/reddi
- İşlem geçmişi

**Şartlar:**
- Kalıtım kullanılmalı
- Hata yönetimi olmalı
- İşlem kayıtları tutulmalı
- Yetersiz bakiye kontrolü

**Öğrenme Hedefleri:**
- Inheritance (kalıtım)
- Polymorphism
- Exception handling
- Logging

---

#### 2.4. Valid Parantezler (Algoritma)

**Problem Tanımı:**
Bir dizedeki parantezlerin ((), {}, []) geçerli olup olmadığını kontrol etme.

**Girdi Formatı:**
- `s`: "()[]{}" veya "([)]"

**Beklenen Çıktı:**
- `True` (geçerli ise)
- `False` (geçersiz ise)

**Şartlar:**
- Sadece (), {}, [] parantezleri
- Açılan parantez kapanmalı
- Doğru sırada olmalı
- Stack kullanılmalı

**Öğrenme Hedefleri:**
- Stack veri yapısı
- Parantez eşleştirme
- LIFO (Last In First Out)
- String parsing

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 2.5. Dosya Organizatörü

**Problem Tanımı:**
Belirtilen bir dizindeki dosyaları türlerine (resim, belge, video vb.) göre otomatik olarak farklı klasörlere taşıyarak düzenleyen ve büyük dosya işlemlerinde performansı artırmak için threading kullanabilen bir araç.

**Girdi Formatı:**
- Kaynak dizin: "/Users/Desktop/Karışık"
- Hedef dizin: "/Users/Desktop/Düzenli"

**Beklenen Çıktı:**
- Düzenlenmiş klasör yapısı
- İşlem raporu
- Hata mesajları

**Şartlar:**
- Dosya türlerine göre sınıflandırma
- Threading kullanımı
- Hata yönetimi
- İlerleme göstergesi

**Öğrenme Hedefleri:**
- OS modülü
- Dosya sistemi işlemleri
- Threading
- Dosya türü tespiti

---

#### 2.6. En Büyük Alt Dizi Toplamı (Algoritma)

**Problem Tanımı:**
Verilen bir dizideki en büyük toplamı olan sürekli alt diziyi bulma.

**Girdi Formatı:**
- `nums`: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

**Beklenen Çıktı:**
- `6` (alt dizi [4, -1, 2, 1] toplamı)

**Şartlar:**
- Kadane algoritması kullanılmalı
- Time complexity: O(n)
- Space complexity: O(1)
- Negatif sayılar olabilir

**Öğrenme Hedefleri:**
- Kadane algoritması
- Dynamic programming
- Subarray kavramı
- Optimization teknikleri

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 2.7. Merge Sorted Listeler (Algoritma)

**Problem Tanımı:**
İki sıralı bağlı listeyi birleştirerek yeni bir sıralı bağlı liste oluşturma.

**Girdi Formatı:**
- `list1`: [1, 3, 5]
- `list2`: [2, 4, 6]

**Beklenen Çıktı:**
- `[1, 2, 3, 4, 5, 6]`

**Şartlar:**
- Linked list manipülasyonu
- Sıralı birleştirme
- Time complexity: O(n + m)
- Space complexity: O(1)

**Öğrenme Hedefleri:**
- Linked list yapısı
- Merge algoritması
- Pointer manipulation
- Sıralı birleştirme

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

### Seviye 3: Web, API ve İleri Algoritmalar

#### 3.1. Basit Web Sunucusu

**Problem Tanımı:**
Flask framework kullanarak HTTP GET/POST isteklerini karşılayabilen, farklı URL'ler için içerik sunabilen basit bir web sunucusu uygulaması.

**Girdi Formatı:**
- URL: "http://localhost:5000/"
- HTTP Method: GET/POST

**Beklenen Çıktı:**
- HTML sayfaları
- JSON responses
- HTTP status codes

**Şartlar:**
- Flask framework kullanılmalı
- En az 3 farklı route olmalı
- GET/POST metodları desteklenmeli
- Template rendering olmalı

**Öğrenme Hedefleri:**
- Flask framework
- HTTP metodları
- Routing
- Template rendering

---

#### 3.2. Ağaç Maksimum Derinliği (Algoritma)

**Problem Tanımı:**
Bir ikili ağacın maksimum derinliğini bulma.

**Girdi Formatı:**
- Binary tree: [3, 9, 20, null, null, 15, 7]

**Beklenen Çıktı:**
- `3` (maksimum derinlik)

**Şartlar:**
- Binary tree yapısı
- DFS/BFS kullanılabilir
- Recursive/iterative çözüm
- Null node kontrolü

**Öğrenme Hedefleri:**
- Binary tree yapısı
- DFS/BFS algoritmaları
- Tree traversal
- Recursion

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 3.3. Hava Durumu Uygulaması

**Problem Tanımı:**
Harici bir hava durumu API'sinden veri çekerek, JSON formatındaki bu veriyi ayrıştırıp, kullanıcıya belirli bir konumun güncel hava durumu bilgilerini gösteren bir uygulama.

**Girdi Formatı:**
- Şehir: "İstanbul"
- API Key: "your_api_key"

**Beklenen Çıktı:**
- Sıcaklık: 25°C
- Nem: %60
- Durum: Güneşli

**Şartlar:**
- API çağrıları yapılmalı
- JSON parsing olmalı
- Hata yönetimi olmalı
- Kullanıcı dostu arayüz

**Öğrenme Hedefleri:**
- API entegrasyonu
- JSON parsing
- Error handling
- HTTP requests

---

#### 3.4. Ters Bağlı Liste (Algoritma)

**Problem Tanımı:**
Verilen bir bağlı listeyi tersine çevirme.

**Girdi Formatı:**
- `head`: 1 → 2 → 3 → 4 → 5

**Beklenen Çıktı:**
- `head`: 5 → 4 → 3 → 2 → 1

**Şartlar:**
- In-place reversal
- Time complexity: O(n)
- Space complexity: O(1)
- Pointer manipulation

**Öğrenme Hedefleri:**
- Linked list manipülasyonu
- Pointer operations
- In-place algorithms
- Iterative/recursive çözüm

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 3.5. Basit Blog Sistemi

**Problem Tanımı:**
Kullanıcıların gönderi oluşturup düzenleyebileceği, verileri SQLite veritabanında saklayan, temel kullanıcı kimlik doğrulama özelliklerine sahip basit bir web tabanlı blog sistemi.

**Girdi Formatı:**
- Kullanıcı girişi
- Blog post oluşturma
- Post düzenleme

**Beklenen Çıktı:**
- Blog postları
- Kullanıcı profilleri
- SQLite veritabanı

**Şartlar:**
- SQLite veritabanı
- CRUD operasyonları
- User authentication
- Web arayüzü

**Öğrenme Hedefleri:**
- SQLite veritabanı
- CRUD operasyonları
- User authentication
- Web development

---

#### 3.6. Tek Sayı Düğümü Bulma (Algoritma)

**Problem Tanımı:**
Bir bağlı listede tekrar etmeyen tek bir sayıyı bulma.

**Girdi Formatı:**
- `head`: 4 → 1 → 2 → 1 → 2

**Beklenen Çıktı:**
- `4` (tekrar etmeyen sayı)

**Şartlar:**
- Hash Table veya XOR kullanılabilir
- Time complexity: O(n)
- Space complexity: O(1) (XOR ile)
- Tek bir sayı tekrar etmiyor

**Öğrenme Hedefleri:**
- Hash Table kullanımı
- XOR bit manipulation
- Frequency counting
- Bitwise operations

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

### Seviye 4: Veri Analizi ve Gelişmiş Uygulamalar

#### 4.1. CSV Veri Analizi

**Problem Tanımı:**
Pandas kütüphanesini kullanarak büyük CSV dosyalarındaki verileri okuyup temizleyebilen, belirli koşullara göre filtreleyebilen, istatistiksel özetler çıkarabilen ve Matplotlib ile bu verileri görselleştiren bir veri analizi aracı.

**Girdi Formatı:**
- CSV dosyası: "sales_data.csv"
- Filtreleme kriterleri

**Beklenen Çıktı:**
- İstatistiksel özetler
- Grafikler ve çizelgeler
- Filtrelenmiş veriler

**Şartlar:**
- Pandas kullanımı
- Matplotlib görselleştirme
- Veri temizleme
- İstatistiksel analiz

**Öğrenme Hedefleri:**
- Pandas kütüphanesi
- Matplotlib görselleştirme
- Veri analizi
- İstatistiksel hesaplamalar

---

#### 4.2. Graf BFS/DFS (Algoritma)

**Problem Tanımı:**
Bir graf üzerinde Genişlik Öncelikli Arama (BFS) ve Derinlik Öncelikli Arama (DFS) algoritmalarını uygulama.

**Girdi Formatı:**
- Graph: adjacency list veya matrix
- Starting node: 0

**Beklenen Çıktı:**
- BFS traversal: [0, 1, 2, 3, 4]
- DFS traversal: [0, 1, 3, 2, 4]

**Şartlar:**
- Adjacency list/matrix kullanımı
- BFS ve DFS implementasyonu
- Time complexity: O(V + E)
- Space complexity: O(V)

**Öğrenme Hedefleri:**
- Graph veri yapısı
- BFS algoritması
- DFS algoritması
- Queue/Stack kullanımı

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 4.3. Basit E-ticaret Sistemi

**Problem Tanımı:**
Ürün listeleme, sepete ekleme, sepeti yönetme gibi temel e-ticaret özelliklerini bir REST API üzerinden sunan, JWT ile kullanıcı kimlik doğrulamasını sağlayan ve ödeme işlemlerini simüle edebilen bir sistem.

**Girdi Formatı:**
- User authentication
- Product selection
- Shopping cart operations

**Beklenen Çıktı:**
- Product catalog
- Shopping cart
- Order confirmation

**Şartlar:**
- RESTful API
- JWT authentication
- Payment simulation
- Database integration

**Öğrenme Hedefleri:**
- REST API tasarımı
- JWT authentication
- E-commerce workflows
- Database operations

---

#### 4.4. Dikdörtgen Alanı (Algoritma)

**Problem Tanımı:**
Verilen bir dizi dikdörtgenin çakışan alanını veya toplam alanını hesaplama.

**Girdi Formatı:**
- `rectangles`: [[0,0,2,2], [1,1,3,3]]

**Beklenen Çıktı:**
- `7` (toplam alan)

**Şartlar:**
- Geometrik algoritmalar
- Sweep line kavramı
- Overlap detection
- Area calculation

**Öğrenme Hedefleri:**
- Geometrik algoritmalar
- Sweep line tekniği
- Overlap detection
- Computational geometry

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 4.5. Web Scraping Uygulaması

**Problem Tanımı:**
BeautifulSoup ve/veya Selenium kütüphanelerini kullanarak belirli web sitelerinden otomatik olarak veri çekebilen ve bu veriyi yapılandırılmış bir formatta kaydedebilen bir web kazıma aracı.

**Girdi Formatı:**
- Target URL: "https://example.com"
- Data selectors: CSS selectors

**Beklenen Çıktı:**
- Scraped data
- Structured output
- CSV/JSON files

**Şartlar:**
- BeautifulSoup kullanımı
- Selenium (gerekirse)
- Data extraction
- Rate limiting

**Öğrenme Hedefleri:**
- Web scraping
- HTML parsing
- Data extraction
- Automation

---

#### 4.6. Minimum Spanning Tree (Algoritma)

**Problem Tanımı:**
Bir grafın minimum yayılan ağacını bulma (örneğin Prim veya Kruskal algoritmaları).

**Girdi Formatı:**
- `graph`: weighted adjacency matrix
- Starting node: 0

**Beklenen Çıktı:**
- MST edges
- Total weight

**Şartlar:**
- Graph algorithms
- Greedy approach
- Union-Find data structure
- Edge sorting

**Öğrenme Hedefleri:**
- MST algorithms
- Greedy algorithms
- Union-Find
- Graph optimization

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

### Seviye 5: İleri Seviye ve Uzmanlaşma

#### 5.1. Mikroservis Mimarisi

**Problem Tanımı:**
Büyük bir uygulamayı, her biri kendi işlevini yerine getiren bağımsız küçük servisler (mikroservisler) halinde tasarlama ve geliştirme. Docker kullanarak bu servisleri izole konteynerlerde çalıştırma.

**Girdi Formatı:**
- Service definitions
- Docker configurations
- API specifications

**Beklenen Çıktı:**
- Microservices
- Docker containers
- Service communication

**Şartlar:**
- Docker containerization
- Service communication
- Load balancing
- Service discovery

**Öğrenme Hedefleri:**
- Microservices architecture
- Docker
- Service communication
- Distributed systems

---

#### 5.2. Machine Learning Projesi

**Problem Tanımı:**
Scikit-learn, TensorFlow veya PyTorch gibi kütüphaneleri kullanarak belirli bir veri seti üzerinde bir makine öğrenimi modeli eğitme ve eğitilen modeli kullanarak tahminler yapabilen bir API servisi oluşturma.

**Girdi Formatı:**
- Training dataset
- Model parameters
- Prediction inputs

**Beklenen Çıktı:**
- Trained model
- Prediction API
- Model performance metrics

**Şartlar:**
- ML library usage
- Model training
- API development
- Model deployment

**Öğrenme Hedefleri:**
- Machine learning
- Model training
- API development
- Model deployment

---

#### 5.3. Kısa Yol Algoritmaları (Algoritma)

**Problem Tanımı:**
Dijkstra veya Bellman-Ford gibi kısa yol algoritmalarını uygulama.

**Girdi Formatı:**
- `graph`: weighted adjacency matrix
- `source`: starting node
- `destination`: target node

**Beklenen Çıktı:**
- Shortest path
- Path distance
- Path reconstruction

**Şartlar:**
- Graph algorithms
- Dynamic programming
- Priority queue
- Path optimization

**Öğrenme Hedefleri:**
- Shortest path algorithms
- Dynamic programming
- Priority queue
- Graph optimization

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

#### 5.4. Real-time Chat Uygulaması

**Problem Tanımı:**
Kullanıcıların anlık mesajlaşabildiği, WebSocket protokolünü kullanarak gerçek zamanlı iletişimi sağlayan, Redis gibi bir önbellek mekanizmasıyla performansı artıran bir chat uygulaması.

**Girdi Formatı:**
- User messages
- Room selection
- Real-time communication

**Beklenen Çıktı:**
- Real-time messaging
- Message history
- User presence

**Şartlar:**
- WebSocket implementation
- Redis caching
- Real-time communication
- Message persistence

**Öğrenme Hedefleri:**
- WebSocket
- Real-time communication
- Redis caching
- Message handling

---

#### 5.5. Network Flow (Algoritma)

**Problem Tanımı:**
Maksimum akış (Max Flow) veya minimum kesit (Min Cut) gibi ağ akış algoritmalarını uygulama.

**Girdi Formatı:**
- `graph`: flow network
- `source`: source node
- `sink`: sink node

**Beklenen Çıktı:**
- Maximum flow value
- Flow assignment
- Min-cut edges

**Şartlar:**
- Network flow algorithms
- Ford-Fulkerson method
- Residual graph
- Min-cut max-flow theorem

**Öğrenme Hedefleri:**
- Network flow
- Ford-Fulkerson
- Residual graph
- Optimization algorithms

**Çözüm İpucu:**
→ CozumYaklasimlari.md dosyasına bak

---

## NOTLAR
- Bu dosya sürekli güncellenecek
- Her proje için detaylı açıklamalar eklenecek
- Çözüm yaklaşımları için ayrı dosyaya bakılacak 