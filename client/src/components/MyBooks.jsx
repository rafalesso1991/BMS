import React, {useEffect, useState} from 'react';
import axios from 'axios';
import useAuth from "../hooks/useAuth";
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button, Modal, TextField } from '@mui/material';
import { Edit, Delete } from '@mui/icons-material';

const BooksData = () => {

  const { token } = useAuth();
  const booksPerPage = 10;
  const [books, setBooks] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [modalCreate, setModalCreate] = useState(false);
  const [modalUpdate, setModalUpdate] = useState(false);
  const [modalDelete, setModalDelete] = useState(false);

  const [bookSelected, setBookSelected] = useState({ title: '', description:'' })

  const handleChange = e => {
    const { name, value } = e.target;
    setBookSelected(prevState => ({
      ...prevState,
      [name]: value
    }))
    console.log(bookSelected);
  }

  useEffect(() => {

    let isMounted = true;
    const controller = new AbortController();

    const handleGet = async() => {
      await axios.get('http://localhost:8000/books/my_books/', { headers: { 'Authorization': 'Bearer ' + token } })
      .then(response => {
        isMounted && setBooks(response.data);
      })
    }
    handleGet();
    return () => {
      isMounted = false
      controller.abort();
    }

  }, [token]);
  // Handle "POST" Requests
  const handlePost = async() => {
    await axios.post('http://localhost:8000/books/new_book/', { headers: { 'Authorization': 'Bearer ' + token } }, bookSelected)
    .then(response => {
      setBooks(books.concat(response.data))
      openCloseModalCreate()
    })
  }
  // Handle "PUT" Requests
  const handlePut = async() => {
    await axios.put(`http://localhost:8000/books/update/${bookSelected.id}`, { headers: { 'Authorization': 'Bearer ' + token } }, bookSelected)
    .then(response => {
      let newData = books;
      newData.map(book => {
        if (bookSelected.id === book.id) {
           book.title = bookSelected.title;
           book.description = bookSelected.description;
        }
        return newData;
      })
      setBooks(newData);
      openCloseModalUpdate();
    })
  }
  // Handle "DELETE" Requests
  const handleDelete = async () => {
    await axios.delete(`http://localhost:8000/books/delete/${bookSelected.id}`, { headers: { 'Authorization': 'Bearer ' + token } })
    .then(response => {
      const updatedBooks = books.filter((book) => book.id !== bookSelected.id);
      setBooks(updatedBooks);
      openCloseModalDelete();
    })
  };
  // Open-Close Create Modal
  const openCloseModalCreate = () => {
    setModalCreate(!modalCreate);
  }
  // Open-Close Update Modal
  const openCloseModalUpdate = () => {
    setModalUpdate(!modalUpdate);
  }
  // Open-Close Delete Modal
  const openCloseModalDelete=() => {
    setModalDelete(!modalDelete);
  }
  // Select Book to Update-Delete
  const selectBook=(book, box) => {
    setBookSelected(book);
    (box === 'Update') ? openCloseModalUpdate() : openCloseModalDelete()
  }
  // Body of the Create Modal
  const bodyCreate = (
    <div style = {{ backgroundColor: 'rgba(255, 255, 255, 0.5)' }}>
      <h3>Add New Book</h3>
      <TextField name = "title" label = "Title" onChange = { handleChange }/>
      <br />
      <TextField name = "description" label = "Description" onChange = { handleChange }/>
      <br /><br />
      <div align="right">
        <Button onClick = { () => handlePost() } color = "primary">Create</Button>
        <Button onClick = { () => openCloseModalCreate() }>Cancel</Button>
      </div>
    </div>
  )
  // Body of the Update Modal
  const bodyUpdate = (
    <div style = {{ backgroundColor: 'rgba(255, 255, 255, 0.5)' }}>
      <h3>Update Book</h3>
      <TextField name = "title" label = "Title" onChange = { handleChange } value = { bookSelected && bookSelected.title }/>
      <br />
      <TextField name = "description" label = "Description" onChange = { handleChange } value = { bookSelected && bookSelected.description }/>
      <br /><br />
      <div align="right">
        <Button onClick = { () => handlePut() } color = "primary">Update</Button>
        <Button onClick = { () => openCloseModalUpdate() }>Cancel</Button>
      </div>
    </div>
  )
  // Body of the Delete Modal
  const bodyDelete = (
    <div style = {{ backgroundColor: 'rgba(255, 255, 255, 0.5)' }}>
      <p>Are you sure you want to delete the book <b>{ bookSelected && bookSelected.title }</b> ? </p>
      <div align="right">
        <Button onClick = { () => handleDelete() } color = "secondary">Yes</Button>
        <Button onClick = { () => openCloseModalDelete() } >No</Button>
      </div>
    </div>
  )
  // PAagination
  const indexLastBook = currentPage * booksPerPage;
  const indexFirstBook = indexLastBook - booksPerPage;
  const currentBooks = books.slice(indexFirstBook, indexLastBook);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <div style = {{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <div>
      <br />
        <Button onClick = { () => openCloseModalCreate() }>Add Book</Button>
      <br /><br />
        <TableContainer component = { Paper }>
          <Table aria-label = "books table">
            <TableHead>
              <TableRow>
                <TableCell style = {{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>ID</TableCell>
                <TableCell style = {{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Title</TableCell>
                <TableCell style = {{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Description</TableCell>
                <TableCell style = {{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Actions</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              { currentBooks.map((book) => (
                <TableRow key = { book.id }>
                  <TableCell>{ book.id }</TableCell>
                  <TableCell>{ book.title }</TableCell>
                  <TableCell>{ book.description }</TableCell>
                  <TableCell>
                    <Edit onClick = { () => selectBook(book, 'Update') }/>
                      &nbsp;&nbsp;&nbsp;
                    <Delete onClick = { () => selectBook(book, 'Delete') }/>
                  </TableCell>
                </TableRow>
              )) }
            </TableBody>

          </Table>

        </TableContainer>

        <div style = {{ display: 'flex', justifyContent: 'center' }}>
          { Array.from({ length: Math.ceil(books.length / booksPerPage) }, (_, i) => (
            <Button key={i + 1} onClick={() => paginate(i + 1)}>
              {i + 1}
            </Button>
          )) }
        </div>

        <Modal 
          open = { modalCreate }
          onClose = { openCloseModalCreate }
          style = {{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          } }>
            { bodyCreate }
        </Modal>

        <Modal
          open = { modalUpdate }
          onClose = { openCloseModalUpdate }
          style = {{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          } }
        >
            { bodyUpdate }
        </Modal>

        <Modal
          open = { modalDelete }
          onClose = { openCloseModalDelete }
          style = {{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}
        >
            { bodyDelete }
        </Modal>

      </div>

    </div>
  
  );

}

export default BooksData;
