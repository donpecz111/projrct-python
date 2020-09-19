class Zespolona:
      def __init__(self ,rzeczywista ,urojona ):
          self.r = rzeczywista
          self.i = urojona

x = Zespolona(3.0,-4.5)
x.r


class MojaKlasa:
    zmienna ="blah"
    def funkcja(self):
        print("To jest wiadomość wewnątrz klasy.")


obiekt = MojaKlasa()
obiekt.zmienna ="Witaj"
print(obiekt.zmienna)

obiekt2 = MojaKlasa()
obiekt2.zmienna = "Żegnaj"
print(obiekt2.zmienna)

obiekt3 =MojaKlasa()
obiekt3.funkcja()
