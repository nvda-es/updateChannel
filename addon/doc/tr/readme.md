# NVDA Güncelleme Kanalı Seçici #

* Yazar: Jose Manuel Delicado
* NVDA uyumluluğu: 2021.3 ve üzeri sürümler
* Kararlı sürümü [stable version][1] indir

Bu eklenti, herhangi bir web sayfasını ziyaret etmeden veya web tarayıcınızı
kullanmadan seçilen türün en son NVDA sürümünü indirip yüklemenizi
sağlar. Örneğin, bir NVDA anlık görüntüsünde yeni özellikleri test etmek ve
ardından en son kararlı sürüme geri dönmek istediğinizde yararlıdır. Düzenli
olarak NVDA anlık görüntülerini test ederseniz ve genellikle bilgisayarınıza
yüklerseniz, bu eklentiyle çok zaman kazanacaksınız. NVDA'nın yüklü
kopyasını değiştirmeden taşınabilir modda anlık görüntüleri test etmeyi
tercih ederseniz, bu eklenti sizin için de geçerlidir.

## Kullanım

Kullanım
NVDA menü, Tercihler, Ayarlar, Güncelleme Kanalı kategorisine giderek NVDA
güncelleme kanalını değiştirebilirsiniz. İstediğiniz kanalı seçtikten ve
Tamam'a bastıktan sonra, bir sonraki otomatik güncelleme kontrolüne kadar
bekleyin veya NVDA yardım menüsüne gidin ve "Güncellemeleri kontrol et"
seçeneğini seçin. Şimdilik, mevcut kanallar şunlardır:

* Varsayılan: Bu, NVDA sürümünüz tarafından kullanılan varsayılan
  kanaldır. Bu seçeneğin seçilmesi, eklentiyi devre dışı bırakmayla aynı
  anlama gelir.
* Kararlı: güncelleme kanalını kararlı olmaya zorla. Anlık görüntüden
  kararlı bir sürüme dönmek istediğinizde kullanışlıdır.
* Kararlı, rc ve beta: Bu beta sürümleri için kanaldır. Yayınlandıktan sonra
  İlk beta sürümünü alacaksınız. Bu kanal, bir sonraki kararlı sürüme
  ulaşana kadar beta ve rc sürümlere güncelleme yapmanıza olanak tanır.
* Alfa (anlık görüntüler): en son alfaya güncellemek için bu seçeneği
  seçin. Alfa anlık görüntüleri yeni özellikleri test etmenizi sağlar ancak
  oldukça kararsızdır. Lütfen dikkatli olun.
* Güncelleştirmeleri devre dışı bırak (önerilmez): Bu seçenek güncelleme
  kanalını devre dışı bırakır. Güncelleştirmeleri denetlerseniz bir hata
  iletisi görüntülenir. Otomatik güncelleştirmeleri Genel ayarlar
  kategorisinden devre dışı bırakabileceğinizi unutmayın. Bu seçeneği
  yalnızca test amacıyla kullanın.

Ayarlar paneli açıldığında, her kanal için mevcut güncellemeler hakkında
bilgi arka planda alınacaktır.
Bu bilgileri görebileceğiniz salt okunur bir düzenleme alanına gitmek için
Sekme tuşuna basın.
Bu bilgiler, seçim kutusundan güncelleme kanalını değiştirdiğinizde dinamik
olarak güncellenecektir.
Seçilen kanal için bir güncelleme varsa, düzenleme alanının yanında bir veya
iki bağlantı görünür:

* İndir: Web tarayıcınızda açmak ve en son yükleyiciyi indirmek için bu
  bağlantı üzerinde boşluk çubuğuna basın.
* Değişiklikleri görüntüle: Web tarayıcınızda Yenilikler belgesini açmak
  için bu bağlantının üzerinde boşluk çubuğuna basın. Bazı kanallar için bu
  bağlantı görüntülenmez.

## Değişiklikler

### Sürüm 1.2

* Çeviriler güncellendi.
* NVDA 2022.1 ile uyumludur.
* Güvenlik nedeniyle minimum NVDA sürümü 2021.3 olarak ayarlandı.
* NV Access sunucusunda, alfa sürümünden kararlı sürüme güncelleme
  yapılırken 2019.2.1 sürümünün sunulmasına neden olan bir hata için geçici
  çözüm.

### Sürüm 1.1

* Desteklenmeyen kanallar kaldırıldı.
* Çeviriler güncellendi.
* Ayarlar paneline mevcut güncellemelerin bilgileri eklendi.

### Sürüm 1.0

* İlk Sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=updchannelselect
