import Router from "express-promise-router";
import  {actulizarTarea, crearTarea, eliminarTarea, listarTarea, listarTareas} from "../controllers/tareas.controllers";
const router = Router();
router.get('/tareas',listarTareas);
router.get ('/tareas/id',listarTarea);
router.post('/tarea',crearTarea);
router.put('/tarea/id',actulizarTarea);
router.delete('/tareas/id',eliminarTarea);

export default router;