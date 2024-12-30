# modbuSIS
modbuSIS yazılımı, TCP/IP ağlarındaki Modbus konuşan cihazları bulur ve kimliklerini listeler. 
Modbus haberleşme protokolünde 43 (Read Device Identification) fonksiyonunu kullanır ve 502 numaralı portu açık cihazlardan kimlik bilgisi ister.
Kimlik bilgisi sorgusuna yanıt veren cihazların kimlik bilgilerini listeler ve ağdaki modbus konuşan cihazların görünmesini sağlar.
Kodun optimizasyonu için timeout değerleriyle oynayabilirsiniz. 
Subnet üzerinden tarama yaptığı için farklı subnetler kullanıyorsanız subnet alanını doğru doldurmanız gerekir. 
Local IP, yazılımın koştuğu bilgisayardaki modbus ağına bağlanmış olan interface anlamına gelir. Örneğin hem ethernet hem de Wİ-Fİ kullanıyorsanız, arayüzden IP'nizi öğrenip Local IP kutusuna o interface'in aldığı IP'yi girmelisiniz. 
Örneğin; Wİ-Fİ adaptörünüz 192.168.1.50 IP'sini almış. Ethernet adaptörünüz ise 192.168.1.20 IP'sini almış. Modbus cihazlarınız ethernet ağında. Bu durumda Local IP alanına 192.168.1.20 girmeniz gerekir. 

Sorularınız için baran@otomasis.email üzerinden iletişime geçebilirsiniz. 
