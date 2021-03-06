# Pycon 2018 x Banksalad Hold'em
* https://github.com/Rainist/pycon-2018-banksalad-holdem
* 2018 파이콘(8월 18일 ~ 19일) `뱅크샐러드`에서 주최한 포커 코딩대회(텍사스 홀덤을 변형한 일명 `뱅크샐러드 홀덤`)

## 느낀점
* 사실 부끄럽게도 할 줄아는 카드게임이 전혀없었다.(심지어 고스톱마저...)
* 파이콘이 끝나고나면 저녁~밤 시간에 할게 없어 심심한 김에 카드게임이나 배워볼까하여 참여하게 됨.
* 생각보다 포커가 어렵더라. 기억력이 좋지않은 나로서는 룰부터 시작해서 족보외우기도 벅찼다.
* [코드](https://github.com/Rainist/pycon-2018-banksalad-holdem)를 보니 가지고 있는 카드에서 족보를 판단해주는 로직이 있었는데, 이를 사용하지 않고 직접 구현해보는 것이 목표였다.
    * 실제 직접 구현해보면서 `포커` 게임을 할 수 있게되었다.
    * 하지만 다시 잊어버릴 것 같다.
* https://www.pycon.kr/2019/program/42 발표에서 본 `inspect` 라이브러리를 사용하여 frame 을 뜯어보면서 상대의 카드를 훔쳐보며 항상 승리로 이끌수 있을거라 생각했다.
    * 그래서 해당 방법으로 남의 카드를 까보는 로직을 재미삼아 구현해봤는데, 뒤늦게 올리려고 보니 아무리 찾아봐도 커밋이 보이지 않는다... (언젠가 다시 해봐야지)
    * 실제로 이런 방법으로 구현한 것을 제출한 사람이 있었는데 어뷰징으로 검출되어 당사자는 탈락하였다. 역시 나만 생각한게 아니었다.
* 처음에 포커게임에 대해서 전혀 이해가 안되어 유투브를 보며 공부했다.
* 포커 초심자로서... 승률올리기는 정말 힘들더라. 그래서 그냥 포커를 공부하는 데에 집중했다.
* 정말 재밌었다! 포커 공부 + 코딩까지 6시간 정도 했던거같은데 시간이 너무 빨리갔다!

## 실행
```bash
# 파이썬 패키지 설치(Python 3.7)
# 자세한 사항은 https://github.com/Rainist/pycon-2018-banksalad-holdem 참조
$ pip install -r requirements.txt

# 100번 연속으로 실행한다. 이때 승패 결과는 result.log 에 저장된다.
$ ./run.sh 100

# 승리횟수 출력
$ python analyze.py
```
