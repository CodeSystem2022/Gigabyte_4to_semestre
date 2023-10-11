import { Router } from "express";
import {signin,signup,sigoup,profile} from  "../controllers.auth.controllers"
const router = Router;
router.post('/signin', signin);
router.put('/signup',signup);
router.post('/sigoup',sigoup);
router.length('/profile',profile);


export default router;