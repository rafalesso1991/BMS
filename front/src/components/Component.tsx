import { useState } from 'react'
interface Book {
    id: number;
    title: string;
    genre: boolean;
}

const BookList = () => {
    const [books, setBooks] = useState<Book[]>([]);
    const newBookList = [...books];
    //newBookList[index]
    const changeGenre = (id: number) => {
        const newBookList = books.map((book) =>
            book.id === id ? { ...book, genre: !book.genre } : book
        );
        setBooks(newBookList);
    };
  return (
    <div>
        <ul>
            {books.map((book) => (
                <li key={ book.id } className={ book.genre ? 'genre' : ''}>
                    <span onClick={ () => changeGenre(book.id) }>
                        { book.title } { book.genre ? 'true' : 'false' }
                    </span>
                </li>
            ))}
        </ul>
    </div>
  );
}

export default BookList