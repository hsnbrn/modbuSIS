# modbuSIS

GPL-3.0 ile lisanslanmıştır. 

Sürümler arasındaki farklar ve güncel sürüm (v1.1) için "Releases" altına bakınız.


AMAÇ:

Modbus, Schneider Electric'in geliştirmiş olduğu endüstriyel bir haberleşme protokolüdür. Bu protokol son yıllarda TCP/IP ağlarında çalışmata ve TCP/IP protokülü ile içe içe geçmiş bulunmaktadır. Bu anlamda, TCP/IP ağlarında /ethernet) kullanılan araçlardan faydalanmak gerekmektedir. Ancak bu araçların kimi ücretli ve kapalı kaynak kodlu, kimi de tüm gereksinimleri karşılamamaktadir. Bu anlamda, ağda Modbus cihazlarını tespit etmek için birkaç hamle gerekmektedir. ModbuSIS yazılımı, ethernet ağlarına ARP anonsları gönderir ve gelen yanıtların içinde Modbbus cihazları varsa bunların kimlik bilgilerini listeler. Bu anlamda bir çaığı doldurmaktadır. 

YÖNTEM:

Sürüm 1.0'da ping scan kullanılmış ve yanıt veren IP'lere Modbus FC43 gönderilmiştir. Gelen yanıtlar listelenir.
Sürüm 1.1'de ise ping scan terkedilmiş ve ARP scan yapılmışır. Ağdaki tüm cihazlar mac/vendor veritabanı ile listelenir ve Modbus cihazları koyu renkte kimlik bilhileri ile listelenir. Sürüm 1.1 Nmap kullanmaktadır. Nmap gereksinimleri kullanıcılara bırakılmıştır. 

KOD YAPISI: 

Python3 ile yazılmıştır. Kaynak kod açık olup GPL-3.0 lisansı ile lisanlanmıştır. 



Windows işletim sistemleri için exe dosyasını kullanabilirsiniz. 
MacOS ve Linux sistemler için derlenmiş kod üretilmemiştir, ancak yazılımın kaynak kodlarını indirip GPL Lisansı'na göre kullanabilirsiniz. 
modbuSIS yazılımı, TCP/IP ağlarındaki Modbus konuşan cihazları bulur ve kimliklerini listeler. 
Modbus haberleşme protokolünde 43 (Read Device Identification) fonksiyonunu kullanır ve 502 numaralı portu açık cihazlardan kimlik bilgisi ister.
Kimlik bilgisi sorgusuna yanıt veren cihazların kimlik bilgilerini listeler ve ağdaki modbus konuşan cihazların görünmesini sağlar.
Kodun optimizasyonu için timeout değerleriyle oynayabilirsiniz. Ayrıca "Slave_id" parametresi default olarak 1 girilmiştir. Gömülü ethernet olmayan cihazlarda (Örneğin Altivar930 serisi sürücülerde) slave_id parametresini cihazın modbus ayarlarındaki id ile eşitlemeniz gerekir. Ya da cihazın id'sini 1'e ayarlamanız gerekir. Program kodlarından slave_id ayarını 255 ya da 254 yaparak farklı sonuçlar alabilirsiniz. 

Sürüm 1.0 Subnet üzerinden tarama yaptığı için farklı subnetler kullanıyorsanız subnet alanını doğru doldurmanız gerekir. 

Sürüm 1.0'da Local IP, yazılımın koştuğu bilgisayardaki modbus ağına bağlanmış olan interface anlamına gelir. Örneğin hem ethernet hem de Wİ-Fİ kullanıyorsanız, arayüzden IP'nizi öğrenip Local IP kutusuna o interface'in aldığı IP'yi girmelisiniz. 
Örneğin; Wİ-Fİ adaptörünüz 192.168.1.50 IP'sini almış. Ethernet adaptörünüz ise 192.168.1.20 IP'sini almış. Modbus cihazlarınız ethernet ağında. Bu durumda Local IP alanına 192.168.1.20 girmeniz gerekir. 

Sorularınız için baran@otomasis.email üzerinden iletişime geçebilirsiniz. 
