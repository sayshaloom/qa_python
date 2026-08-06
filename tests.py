from main import BooksCollector

import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тестируем добавление 1 новой книги
    def test_new_book_is_added_to_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('The Third Policeman')
        assert len(collector.get_books_genre()) == 1

    # тестируем добавление книги, которая уже есть в списке
    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('The Third Policeman')
        collector.add_new_book('The Third Policeman')
        assert len(collector.get_books_genre()) == 1

    # тестируем добавление книги с пустым или очень длинным названием
    @pytest.mark.parametrize('title', ['', 'A Very Long And Eleborate Title For A Book', 
                                       'So Very Long And Elaborate Title For A Book'])
    def test_add_book_with_long_title(self, title):
        collector = BooksCollector()
        collector.add_new_book(title)
        assert len(collector.get_books_genre()) == 0

    # тестируем присвоение жанра книге, которая уже есть в списке
    @pytest.mark.parametrize('genre, expected_genre', [['Мультфильмы', 'Мультфильмы'],  ['Фэнтези', '']])
    def test_set_book_genre_for_existing_book(self, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book('The Wind in the Willows')
        collector.set_book_genre('The Wind in the Willows', genre)
        assert collector.get_book_genre('The Wind in the Willows') == expected_genre

    # тестируем присвоение жанра книге, которой нет в списке
    def test_set_genre_for_non_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('The Wind in the Willows', 'Мультфильмы')
        assert collector.get_books_genre() == {}

    # тестируем получение жанра книги, которая есть в списке
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Der Sandmann')
        collector.set_book_genre('Der Sandmann', genre)
        result = collector.get_books_with_specific_genre(genre)
        assert 'Der Sandmann' in result

    # тестируем получения детских книг, когда в списке есть книги с жанрами, которые не подходят детям
    def test_get_books_for_children_with_non_child_friendly_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Der Sandmann')
        collector.set_book_genre('Der Sandmann', 'Ужасы')
        collector.add_new_book('The Wind in the Willows')
        collector.set_book_genre('The Wind in the Willows', 'Мультфильмы')
        result = collector.get_books_for_children()
        assert 'Der Sandmann' not in result
        assert 'The Wind in the Willows' in result

    # тестируем добавление книги в Избранное, когда книга есть в списке
    def test_add_existing_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('The Idiot')
        collector.add_book_in_favorites('The Idiot')
        assert 'The Idiot' in collector.get_list_of_favorites_books()

    # тестируем добавление книги в Избранное, когда книги нет в списке
    def test_add_non_existing_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('The Idiot')
        assert 'The Idiot' not in collector.get_list_of_favorites_books()

    # тестируем повторное добавление книги в Избранное, когда книга уже есть в списке
    def test_add_existing_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('The Idiot')
        collector.add_book_in_favorites('The Idiot')
        collector.add_book_in_favorites('The Idiot')
        assert len(collector.get_list_of_favorites_books()) == 1

    # тестируем удаление книги из Избранного, когда книга есть в списке
    def test_delete_existing_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('The Idiot')
        collector.add_book_in_favorites('The Idiot')
        collector.delete_book_from_favorites('The Idiot')
        assert 'The Idiot' not in collector.get_list_of_favorites_books()