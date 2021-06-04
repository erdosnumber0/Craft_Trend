# Project_3 Craft_Trend
  ## 온라인 공예 클래스 트랜드 분석

<img src="https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=capsule%20render&fontSize=90" />



[![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=black)](github.com/Joowon0220/TODO-List)

[![Vue](/images/vue.png)](https://kr.vuejs.org/)

[![Vue](/https://user-images.githubusercontent.com/76681523/120769873-8428ea80-c558-11eb-8adc-ae0511692654.png)](https://www.slideshare.net/BoramLee69/craft-online-class-trend-analysis)

----------------------
![KakaoTalk_20210604_171524692_01](https://user-images.githubusercontent.com/76681523/120769873-8428ea80-c558-11eb-8adc-ae0511692654.png)(https://www.slideshare.net/BoramLee69/craft-online-class-trend-analysis)

![KakaoTalk_20210604_171524692](https://user-images.githubusercontent.com/76681523/120769948-96a32400-c558-11eb-8601-61614f6de3e7.png)


[![웹페이지로 바로가기](https://drive.google.com/file/d/1tbZ01_ZUNE-9h_JJVTasTKAEDUsZ4UuU/view?usp=sharing)](https://infogram.com/--1hdw2jpxjp00j2l?live)
 
[![PPT](https://drive.google.com/file/d/1u1Zw3flbly82b2aWL1Dz9jZSsD_BJg_P/view?usp=sharing)]
-----------------

----------------
## 1. About: 기록을 시작하며,

- 다른 컨설팅 회사가 받은 의뢰를 학원에서 재수주받아, K-training 과정의 끝자락에 진행한 세번째 프로젝트에 해당하는 기록이다.

- 팀원: 김교건, 노규만, 이보람, 전정재, 정지윤
----------------------------

## 2. From, where? 어디서 왔을까

- 본래 분석을 의뢰한 의뢰 기업은 울산에 위치한 문화센터로, 현재까지 여성을 주 타겟으로 공예에 대한 수업을 주관해 온 기관이다. 대표적인 수업으로 원-데이 취미반, 자격증 취득반, 방과 후 수업 강사 양성반을 운영 중에 있다.
----------------------------
## 3. So, what? 
 
 - (수정- 6)

- 첫번째, 어떤 것을 찾아야 할까 
	- 프로젝트의 골자가 되는 요구사항은 온라인 강좌 진출을 위한 시장 조사이다. 해당 시장은 소수 기업들에 의해 과점된 상태이며, 의뢰기업이 이를 극복하고 새로운 강자로 떠오르게 하기 위해서는 매력적인 경쟁력을 획득해 수요 고객들을 끌어모으기 위한 특장점을 가져야 한다.
	- 후발주자의 이점을 극대화하기 위해서는 제품 컨셉 단계에서의 차별화를 꾀해 선발기업 추월효과를 얻어내야만 한다. 즉, 그 동안 소비자 니즈가 있음에도 불구하고 선두기업에 제공하고 있지 않은 서비스가 있다면 이를 파고들어야 하는 것이다.
	- 하지만 지나친 혁신은 오히려 기존의 서비스에 익숙해져 있던 고객들이 더 외면하게 만드는 효과만 야기할 뿐이다. 경쟁업체와 비교가 불가능한 수준의 차별이 이루어지면 소비자 입장에서는 오버슈팅(over-shooting)이 될 수 있다. 또한 아예 새로운 시장을 창조하는 블루오션 시프트(blue ocean shift) 전략을 권하기에는 인력도, 자금도 부족한 수준이며 바람직하지도 않은 방향이라고도 할 수 있다. 즉, 지나친 혁신보다는 철저하게 현실적으로 충분히 매력적인 서비스를 제공하며 동시에 틈새를 찾아 공략하는 전략이 해당 기업에게는 훌륭한 블루오션 전략에 해당한다고 할 수 있다.

- 두번째, 어떻게 찾아야 할까.
	- 비정형 데이터의 정형화: 현재 가장 활발하게 강의 설립과 구매가 이루어지고 있는 온라인 사이트에서 강좌의 현황과 이에 대한 리뷰 작성글 등 비정현 데이터를 정형화해 해당 강좌들의 장/단점을 시각화해야 한다.
		- 구체적으로는 첫째, 해당 사이트에서 공예와 관련된 카테고리를 만들고 강좌명, 좋아요 혹은 별점, 후기/댓글의 내용과 날짜를 웹 크롤링해 축적하고,
		- 둘째, 크롤링한 텍스트 데이터를 분석이 용이하게 원형 형태소로 바꾸고, 불필요한 단어들을 제거하여 전처리를 진행한다.
		- 셋째, 앞서 전처리한 데이터를 이용하여 감성 사전을 구축하고, 이 감성 사전을 통하여 수강생들의 긍정 포인트와 부정 포인트를 분석한 뒤,
		- 마지막으로는 SNS를 이용한 사회 연결망 분석으로 현재 공예 강좌에서 인기가 있는 것들을 인사이트로 제공해야 한다.
		
------------------------------
## 4. But, why? 왜 하필 온라인 공예 클래스라는 걸까? 통할 것인가?

- (수정-8)

- 작년 한해 동안 참 많은 일상들이 변화하였다. 집에서 업무를 처리해 가는 우리들의 어색한 모습들은 어느새 익숙함을 넘어 당연한 모습이 되었고, 어찌보면   친구들보다는 가족들과 보내는 시간이 많아졌다. 밖에 나가질 못하니 집을 꾸미기 시작했고, 덕분에 인테리어 시장은 전에 없을 호황을 누리고 있다. 무엇보다도 일상을 즐기질 못하니 스트레스를 풀 방도를 못 찾고, 쌓여가는 부정적인 감정들에 우울감을 호소하는 이들이 점차 증가하고 있다. 이처럼, 당연하게 느껴졌던 일상을 박탈당한 뒤 우리에게 다가온 이가 바로 코로나 블루라는 질병이다.
	
	- 이를 해소하기 위해 많은 이들이 택한 방법이 바로 이 온라인 취미 클래스이다. 해소되지 않는 우울감을 극복하기 위한 방안 중 하나로 집에서 취미생활을 즐기고 싶어 하는 사람들이 많아지며 온라인으로 취미생활을 하는 수강생들이 점차 증가하고 있는 것이다. 이에 따라 기존에는 당연히 오프라인 클래스를 검색해보던 이들이, 점차 대안을 찾아 온라인 클래스 홈페이지의 문을 두드리고 있다. 
	- 많은 사람들이 온택트 클래스를 이용하는 이유 또한 다양하다. 
		- 첫째, 합리적인 가격으로 취미생활을 즐길 수 있다는 점이다. 한 클래스가 한 달에 5만 원 정도로 오프라인에서 그림이나 악기를 배우기 위해 학원을 등록하는데 드는 비용보다 훨씬 저렴하다. 
		- 두번째, 자신의 뜻에 따라 자유롭게 수준을 맞출 수 있다. 간단하게 그 분야의 수업을 흥미 위주로 들을 수 있는 원데이 클래스, 그것이 아니라면 보다 깊은 수준의 클래스, 혹은 자격증 교육을 원하는 것인지에 따라 다른 교육을 자유롭게 수강할 수 있는 장점이 있다. 
	- 현재 온라인 취미 클래스를 서비스하고 있는 플랫폼에는 ‘클래스101’, ‘하비풀’, ‘마이비스킷’, ‘탈잉’ 등이 있다. 뜨개질, 그림, 요리 등의 일반적인 취미부터 폴댄스, 타로, 마술 등 독특하고 다양한 종류의 취미 활동을 각 분야의 전문가들에게 배울 수 있다.  이처럼 시대적 특징과 여러가지 장점들이 합쳐져서 온라인 취미 클래스는 앞으로 약 4년 뒤인 2026년에는 670억 규모의 시장을 형성할 것으로 예상하고 있다. 
	-  여기에서 우리는 스스로의 역할을 두고 온라인 시장 진출에 필요한 조사를 수행하는 것이라고 정의할 수 있다. 

## 5.  나가며:

하루를 세며 돌아보던 길 위에서, 언젠가는 이 타임머신 상자를 다시 꺼내 보고 누군가는 웃을 수 있기를 간절히 기도합니다. 


	


