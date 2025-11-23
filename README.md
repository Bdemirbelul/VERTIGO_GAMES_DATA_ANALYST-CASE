In this task, I built a simulation-based A/B test analysis. Starting only with the four retention points (D1, D3, D7, D14), I constructed a realistic piecewise exponential retention curve for each variant, allowing me to estimate the proportion of each cohort that remains active on every day—essential for calculating DAU. Then, I created a model where 20,000 new users join each day and tracked the behavior of these cohorts over time, enabling me to compute the Daily Active Users for both Variant A and Variant B.On the monetization side, I modeled daily revenue using a simple yet mobile-gaming-appropriate formula based on purchase rate and ad revenue:
DAU × purchase rate + DAU × impressions × (eCPM / 1000).After establishing this foundation, I simulated the three scenarios required in the task separately: the baseline flow, the 10-day sale period, and the new traffic source starting from Day 20. For each scenario, I analyzed both the daily and cumulative revenue differences between the two variants.Finally, I visualized the resulting DAU and cumulative revenue curves to make the behaviors of Variant A and Variant B comparable in both the short term and over a 30-day horizon. In this way, I answered all task questions using a data-driven simulation model that is both logical and internally consistent.

## f) Which one should you prioritize, and why? If you could only make one of these improvements:
Kısa vadede para getirmesi açısından sale çok daha yüksek bir katkı sağladığı için, eğer tek bir değişiklik yapacaksam 10 günlük sale’i seçerim çünkü hızlı, doğrudan ve en yüksek ek geliri yaratıyor.





<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/0fae33c6-98ad-497f-853d-c2a85a414ca3" />
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/6ad5752c-0638-491e-9d6d-bef7e39a86b0" />
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/705aaa58-187d-428f-9b55-04f70f6455b2" />
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/0f2a0c8a-960c-414b-a97c-1d06a0117d9d" />




