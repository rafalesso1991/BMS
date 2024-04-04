import BookSection from "./BookSection";
const BookList = () => {
    return (
        <BookSection title="Book List">
            <div>
                <div>Search By</div>
                <input type="text" />
                <select name="SearchBy" className="w-full">
                    <option>Title</option>
                    <option>Author</option>
                    <option>Gender</option>
                    <option>Year</option>
                </select>
            </div>
        </BookSection>
    )
};
export default BookList;