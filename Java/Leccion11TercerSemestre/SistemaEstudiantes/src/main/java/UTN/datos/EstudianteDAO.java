package UTN.datos;

import UTN.dominio.Estudiante;

import static UTN.conexion.Conexion.getConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class EstudianteDAO {
    //Metodo listar
    public List<Estudiante> listarEstudiantes(){
        List<Estudiante> estudiantes = new ArrayList<>();
        // Creamos algunos objetos que son necesarios para la comunicación cono la base de datos.
        PreparedStatement ps; // Envía la sentencia a la base de datos.
        ResultSet rs; // Se obtiene el resultado de la base de datos.
        // Se rea un objeto de tipo conexión
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022";
        try{
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2022"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //Falta agregarlo a la lista
                estudiantes.add(estudiante);
            }
        }catch(Exception e){
            System.out.println("Ocurrio un error al seleccionar datos: " + e.getMessage());
        }
        finally {
            try{
                con.close();
            }catch(Exception e){
                System.out.println("Ocurrio un error al cerrar la conexion con la base de datos: " + e.getMessage());
            }
        }
        return estudiantes;
    }//Fin metodo listar

    //Metodo por id -> find by id
    public boolean buscarEstudiantePorId(Estudiante estudiante){
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 WHERE idestudiantes2022=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery();
            if (rs.next()) {
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true; //se encontro un registro
            }
        } catch (Exception e) {
            System.out.println("Ocurrio un error al buscar estudiante: "+e.getMessage());
        }
        finally{
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("ocurrio un error al cerrar conexion"+e.getMessage());
            }//fin catch
        }//fin finally
        return false;
    }
    //Metodo agregar un nuevo estudiante
    public boolean agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES(?, ?, ?, ?)";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.execute();
            return true;
        }catch(Exception e){
            System.out.println("Ocurrio un error al agregar estudiante: "+e.getMessage());
        }//Fin catch
        finally{
            try{
                con.close();
            }catch(Exception e){
                System.out.println("Error al cerrar la conexion: "+e.getMessage());
            }//Fin catch
        }//Fin finally
        return false;
    }//Fin metodo agregarEstudiante
    // Método para modificar estudiante
    public boolean modificarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "UPDATE estudiantes2022 SET nombre=?, apellido=?, telefono=?, email=? WHERE idestudiantes2022=?";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.setInt(5, estudiante.getIdEstudiante());
            ps.execute();
            return true;
        } catch (Exception e){
            System.out.println("Error al modificar estudiante: "+e.getMessage());
        } // Fin catch
        finally {
            try {
                con.close();
            } catch (Exception e){
                System.out.println("Error al cerrar la conexión: "+e.getMessage());
            } // Fin catch
        } // Fin finally
        return false;
    } // Fin método modificarEstudiante

    public boolean eliminarEstudiantes(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "DELETE FROM estudiantes2022 WHERE idestudiantes2022=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1,estudiante.getIdEstudiante());
            ps.execute();
            return true;
        }catch (Exception e){
            System.out.println("Error al eliminar estudiante: "+e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("error al cerrar la conexion: "+e.getMessage());
            }
        }
        return false;
    }

    public static void main(String[] args){

        var estudianteDao = new EstudianteDAO();

        //Modificar estudiante
        //var estudianteModificado = new Estudiante(1, "Juan Carlos", "Juarez", "55545665", "jjuarez@mail.com");
        //var modificado = estudianteDao.modificarEstudiante(estudianteModificado);
        //if (modificado)
        //    System.out.println("Estudiante modificado: " + estudianteModificado);
        //else
        //    System.out.println("No se modificó el estudiante: " + estudianteModificado);


        //Agregar estudiante
        //var nuevoEstudiante = new Estudiante("Carlos", "Lara", "5495544223", "carlosl@mail.com");
        //var agregado = estudianteDao.agregarEstudiante(nuevoEstudiante);
        //if(agregado)
         //   System.out.println("Estudiante agregado: "+nuevoEstudiante);
        //else
         //   System.out.println("No se ha agregado estudiante: "+nuevoEstudiante);

        //Eliminar estudiante con id 3
        var estudianteEliminar = new Estudiante(3);
        var eliminado = estudianteDao.eliminarEstudiantes(estudianteEliminar);
        if(eliminado)
            System.out.println("estudiante eliminado: "+estudianteEliminar);
        else
            System.out.println("No se elimino estudiante: "+estudianteEliminar);

        //Listar los estudiantes
        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudianteDao.listarEstudiantes();
        estudiantes.forEach(System.out::println); //Función Lambda para imprimir
    }
}