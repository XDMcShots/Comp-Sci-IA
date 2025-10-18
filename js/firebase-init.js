API_KEY = "AIzaSyADnUUKnmXg36Ln8Wr6q7O7CY05fAh0lUs";
AUTH_DOMAIN = "green-cycle-drive-a674c.firebaseapp.com";
PROJECT_ID = "green-cycle-drive-a674c";
STORAGE_BUCKET = "green-cycle-drive-a674c.firebasestorage.app";
MESSAGING_SENDER_ID = "328391968795";
APPID = "1:328391968795:web:2f095fdd3937e309eb10be";

const firebaseConfig = {
  apiKey: API_KEY,
  authDomain: AUTH_DOMAIN,
  projectId: PROJECT_ID,
  storageBucket: STORAGE_BUCKET,
  messagingSenderId: MESSAGING_SENDER_ID,
  appId: APPID,
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);

let auth = null;
if (firebase.auth) {
  auth = firebase.auth();
  auth.setPersistence(firebase.auth.Auth.Persistence.SESSION);
}

const db = firebase.firestore();
