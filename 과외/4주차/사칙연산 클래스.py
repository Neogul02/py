# 클래스를 어떻게 만들지 먼저 구상하기
# 클래스는 무작정 만드는 것보다 클래스로 만든 객체를
# 중심으로 어떤 식으로 동작하게 할것인지 미리 구상을 한 후에 생각한 것들을 하나씩 해결하면서 완성해 나가는 것이 좋다.


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


a = FourCal()
