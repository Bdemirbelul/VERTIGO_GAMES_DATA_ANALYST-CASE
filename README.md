Bu taskte simülasyon tabanlı bir A/B test analizi kurdum. Önce sadece dört retention noktasından (D1, D3, D7, D14) yola çıkarak her varyant için gün gün ilerleyen, gerçekçi bir piecewise exponential retention eğrisi oluşturdum; çünkü DAU hesaplayabilmek için her cohort'un her gün hayatta kalan kısmını bilmek gerekiyor. Ardından her gün 20.000 yeni kullanıcının eklendiği bir model kurarak bu cohort’ların zaman içindeki davranışlarını takip ettim ve böylece Variant A ile Variant B’nin günlük aktif kullanıcı sayılarını hesapladım. Monetizasyon tarafında ise günlük geliri, sadece satın alma oranı ve reklam gelirinden oluşan basit ama mobil oyun sektörüne uygun bir formülle modelledim: DAU çarpı purchase rate artı DAU çarpı impression çarpı eCPM/1000. Bu temeli oluşturduktan sonra taskte istenen üç farklı senaryoyu baseline akış, 10 günlük sale dönemi ve 20. günden itibaren gelen yeni trafik kaynağı ayrı ayrı simüle ederek hem günlük hem kümülatif gelir tarafındaki farkları analiz ettim. Son olarak, ortaya çıkan DAU ve kümülatif gelir sonuçlarını grafikle görselleştirip Variant A ve B'nin davranışlarını hem kısa vadede hem de 30 günlük uzun vadede karşılaştırılabilir hale getirdim. Bu sayede, taskteki tüm soruları veri odaklı bir simülasyon modeliyle hem mantıklı hem de tutarlı şekilde yanıtlamış oldum.



<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/0fae33c6-98ad-497f-853d-c2a85a414ca3" />
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/6ad5752c-0638-491e-9d6d-bef7e39a86b0" />
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/705aaa58-187d-428f-9b55-04f70f6455b2" />
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/0f2a0c8a-960c-414b-a97c-1d06a0117d9d" />


