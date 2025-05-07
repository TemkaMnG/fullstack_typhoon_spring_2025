import datetime

class Nom:
    def __init__(self, title, author, pages, published_year):
        self.title = title
        self.author = author
        self.pages = pages
        self.published_year = published_year

    def nas(self):
        """Номын насыг олно."""
        try:
            одоогийн_он = datetime.datetime.now().year
            return одоогийн_он - self.published_year
        except Exception as e:
            print(f"Алдаа гарлаа (Нас тооцоолоход): {e}")
            return 0

    def urt_esekh(self):
        """Хуудасны тоо 300-аас их эсэхийг шалгана."""
        return self.pages > 300

    def __str__(self):
        """Номын мэдээллийг тэмдэгт мөрөөр харуулна."""
        return (f"Гарчиг: {self.title}, Зохиолч: {self.author}, "
                f"Хуудас: {self.pages}, Хэвлэгдсэн он: {self.published_year}, "
                f"Нас: {self.nas()} жил, Урт: {'Тийм' if self.urt_esekh() else 'Үгүй'}")

# 3 ном үүсгэх
nom1 = Nom("Clean Code", "Robert C. Martin", 464, 2008)
nom2 = Nom("The Little Prince", "Antoine de Saint-Exupéry", 96, 1943)
nom3 = Nom("Introduction to Algorithms", "Thomas H. Cormen", 1312, 1990)

# Номын мэдээлэл хэвлэх
print(nom1)
print(nom2)
print(nom3)
