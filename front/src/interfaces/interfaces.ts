// DATOS de los Libros
export interface BookData {
    title: string;
    author: string;
    genre: string;
    year: number;
    owner_id: number;
    created_at: number;
    updated_at: number;
}
// ESTADO de los Libros
export interface BookState {
    users: BookData[],
}
// DATOS de los Usuarios
export interface UserData {
    id: number;
    username: string;
    password: string;
    email: string;
    admin: boolean;
    created_at: number;
    updated_at: number;
    logged_in: boolean;
}
// ESTADO de los Usuarios
export interface UserState {
    users: UserData[],
}