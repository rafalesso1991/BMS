import React from 'react';

function Home() {
  return (
    <div style={{ fontSize: '2em', display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', padding: '50px' }}>
      <div>
        <h1>BMS - Book Managment System</h1>
        <h2>Ejercicio de Programación: Sistema de Gestión de Libros con Autenticación</h2>
        <h3>Desarrollo del frontend utilizando react</h3>
        <h4>Objetivo:</h4>
        <p>
          Desarrollar una aplicación web utilizando React.js que incluya funcionalidades de autenticación, gestión de libros y comunicación con una base de datos a través del backend utilizando <b>Axios</b>. <br/>
          Se espera que los participantes utilicen <b>Context API</b> para gestionar el estado de autenticación, implementen un <b>sistema de enrutamiento</b> y realicen llamadas al backend para obtener y manipular datos.</p>
        <h4>Rquisitos Funcionales:</h4>
        <h5>1. Página de Inicio:</h5>
        <p>
          Crear una página principal con una <b>barra de navegación</b> que contenga un <b>botón "Login"</b>.
        </p>
        <h5>2. Autenticación:</h5>
        <p>
          Al presionar el botón "Login", mostrar un <b>formulario</b> que solicite el <b>nombre de usuario (email)</b> y <b>contraseña</b>. <br/>
          Validar que el campo de correo electrónico sea un <b>formato de email válido.</b> <br/>
          <b>Validar las credenciales</b> del usuario en la <b>base de datos</b>. <br/>
          En caso de <b>credenciales incorrectas</b>, mostrar un <b>mensaje de error</b>. <br/>
          En caso de <b>credenciales correctas</b>, cambiar la barra de navegación mostrando dos nuevos botones: <b>"Mis Libros"</b> y <b>"Desconectar"</b>.
        </p>
        <h5>3. Listado de Libros:</h5>
        <p>
          Al presionar el botón "Mis Libros", mostrar una tabla paginada con las columnas <b>"Nombre"</b>, <b>"Descripción"</b> y <b>"Acciones"</b>. <br/>
          Listar los libros desde la base de datos, mostrando solo <b>10 libros</b> por página. <br/>
          Implementar paginación para navegar entre las distintas páginas de libros. <br/>
        </p>
        <h5>4. Agregar Libro:</h5>
        <p>
          Encima de la tabla de libros, incluir un botón <b>"Agregar Libro"</b>. <br/>
          Al presionar el botón, abrir un modal que solicite el <b>nombre</b> y la <b>descripción</b> del libro. <br/>
          Incluir un botón <b>"Agregar"</b> en el modal para añadir el nuevo libro a la base de datos. <br/>
        </p>
        <h5>5. Acciones en la Tabla de Libros:</h5>
        <p>
          En la columna <b>"Acciones"</b> de la tabla, agregar dos botones: <b>"Editar"</b> y <b>"Eliminar"</b>. <br/>
          Al presionar el botón "Editar", abrir un <b>modal</b> que muestre los <b>datos actuales</b> del libro permitiendo al usuario <b>realizar cambios</b> y <b>guardarlos en la base de datos</b>. <br/>
          Al presionar el botón "Eliminar", mostrar un <b>modal de confirmación</b> antes de eliminar el libro de la base de datos. <br/>
        </p>
        <h4>Requisitos Técnicos:</h4>
        <p>
          Utilizar <b>Context API</b> para gestionar el estado de autenticación en la aplicación. <br/>
          Emplear <b>Axios</b> para realizar llamadas al backend y obtener/guardar datos en la base de datos. <br/>
          Implementar <b>enrutamiento</b> para mostrar los diferentes componentes de la aplicación <b></b>según la autenticación del usuario. <br/>
        </p>
      </div>
    </div>
  );
}

export default Home;
