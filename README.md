< 소프트웨어 프로젝트 문제 1 >

# [ 개발 기록 ]
### 09.20
* 본 프로그램 설계 구성 완료
* 구성 : user - gui - operator - data
* gui 객체 구성
    ㄴ 모든 gui 객체는 gui_manager 클래스의 static 딕셔너리로 단 1개만 생성되며 오로지 place 방식으로 배치를 구성한다
    ㄴ gui 객체는 해당 값을 내부 변수(딕셔너리)로 소유하여야 한다.
        -- POS --
        1. x (절대 좌표 X)
        2. y (절대 좌표 Y)
        **3. relx (상대 좌표 X)**
        **4. rely (싱대 좌표 Y)**

        -- SIZE --
        **5. width (너비)**
        **6. height (높이)**ㄴ

        -- VALLUE --
        **7. value (사용자 지정 값)**
        **8. call (value의 값을 결정하는 함수)**

    ㄴ gui 객체에 대하여 배치 함수가 필요함 (배치 함수는 객체 내 POS 딕셔너리와 SIZE 딕셔너리에 의해 결정되며, VALUE 변수는 딕셔너리로 지정하지 않고 따로 value, call로 구분한다)
    ㄴ 배치 함수를 수행할 때 객체 내 call함수를 호출시켜 value의 값을 지정하여 데이터를 항상 최신화 한다.
    ㄴ Call함수는 주로 operation_manager의 함수를 호출하는 역할을 수행한다.

### 09.21
* GUI 초기 화면 제작중