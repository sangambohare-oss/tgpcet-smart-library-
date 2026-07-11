import { initializeApp } from "firebase/app";
import { getDatabase, ref, set, push } from "firebase/database";

const firebaseConfig = {
  apiKey: "YOUR_KEY",
  authDomain: "your-app.firebaseapp.com",
  databaseURL: "https://your-app.firebaseio.com",
  projectId: "your-app",
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

/* Save AI result */
export function saveResult(data){
    const newRef = push(ref(db, "diseaseData"));
    set(newRef, {
        ...data,
        time: Date.now()
    });
}