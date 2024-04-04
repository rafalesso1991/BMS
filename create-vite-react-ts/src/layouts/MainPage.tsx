import BookData from "../components/BookData";
import BookList from "../components/BookList";
import Navbar from "../components/Navbar";
import OwnnerList from "../components/OwnerList";
const MainPage = () => {

    return (
        <>
            <div className="Container">
                <Navbar />
            </div>
            <div className="Container">
                <BookList />
                <BookData />
            </div>
            <div className="Container">
                <OwnnerList />
            </div>
        </>
    )
};
export default MainPage;