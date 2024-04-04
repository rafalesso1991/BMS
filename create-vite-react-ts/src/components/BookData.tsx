import { useState } from "react";

const BookData = () => {
    const [inputValues, setInputValues] = useState({
        title: '',
        author: '',
        year: ''
    })
    const handleSubmit = () =>{
        alert('¿Estás seguro?');
    }
    const handleChange = (ev: React.ChangeEvent<HTMLInputElement>) => {
        setInputValues({
            ...inputValues,
            [ev.target.name]: ev.target.value
        })
    }
    const handleClick = () => {
        alert('¿Estás seguro?');
    }
    return (
        <div>
            <form action="" onSubmit={handleSubmit}>
                <fieldset>
                    <div className="flex">
                        <input onChange={handleChange} value={inputValues.title} type="text" name="Title" placeholder="Title" />
                    </div>
                    <div className="flex">
                        <input onChange={handleChange} value={inputValues.author} type="text" name="Author" placeholder="Author" />
                    </div>
                    <div className="flex">
                        <select name="Genre" id="1">
                            <option value="Adventure">Adventure</option>
                            <option value="Comedy">Comedy</option>
                            <option value="Drama">Drama</option>
                            <option value="Fantasy">Fantasy</option>
                            <option value="Horror">Horror</option>
                            <option value="Romance">Romance</option>
                            <option value="Science Fiction">Science Fiction</option>
                            <option value="Thriller">Thriller</option>
                        </select>
                    </div>
                    <div className="flex">
                        <input onChange={handleChange} value={inputValues.year} type="text" name="Year" placeholder="Year" />
                    </div>
                    <div>
                        <button type="submit" onClick={handleSubmit}>Create</button>
                        <button type="submit" onClick={handleSubmit}>Update</button>
                        <button type="button" onClick={handleClick}>Delete</button>
                    </div>
                </fieldset>
            </form>
        </div>
    )
};
export default BookData;