from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self): #0
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_same_books(self): #1
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating(self): #2
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 10)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 10

    def test_set_book_rating_set_rating_above_ten(self): #3
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != 11

    def test_set_book_rating_set_rating_below_one(self): #4
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != 0

    def test_set_book_rating_set_rating_book_not_in_list(self): #5
        collector = BooksCollector()
        collector.set_book_rating('Хоббит', 8)
        assert collector.get_book_rating('Хоббит') != 8

    def test_get_book_rating_check_rating_if_books_not_added(self):  #6
        collector = BooksCollector()
        assert collector.get_books_rating() != 1

    def test_get_books_with_specific_rating_check_rating_by_one(self): #7
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Хоббит')
        collector.add_new_book('Властелин колец')
        collector.set_book_rating('Хоббит', 7)
        collector.set_book_rating('Властелин колец', 8)
        for i in 'Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить':
            assert i in collector.get_books_with_specific_rating(1)

    def test_add_book_in_favorites_add_two_books(self): #8
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Властелин колец')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_book(self): #9
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert len(collector.get_list_of_favorites_books()) == 1