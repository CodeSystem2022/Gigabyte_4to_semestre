package utn.estudiantes;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.servicio.EstudianteServicio;
import utn.estudiantes.modelo.Estudiantes2022;
import java.util.List;
import java.util.Scanner;


@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner {
	@Autowired
	private EstudianteServicio estudianteServicio;
	private static final Logger logger = LoggerFactory.getLogger(EstudiantesApplication.class);

	String nl = System.lineSeparator();


	public static void main(String[] args) {
		logger.info("Iniciando la aplicacion...");
		//Levantar la fabrica de Spring
		SpringApplication.run(EstudiantesApplication.class, args);
		logger.info("Aplicacion finalizada!");

	}

	@Override
	public void run(String... args) throws Exception {
		logger.info(nl+"Ejecutando el metodo ..run.. de Spring"+nl);
		var salir = false;
		var consola = new Scanner(System.in);
		while (!salir){
			mostrarMenu();
			salir = ejecutarOpciones(consola);
			logger.info(nl);
		}//fin cilco while
	}

	private void mostrarMenu() {
		//logger.info(nl);
		logger.info("""
    			*********Sistema de estudiantes*********
    			1. Listar estudiante
    			2. Buscar estudiante
    			3. Agregar estudiante 
    			4. Modificar estudiante
    			5. Eliminar Estudiante
    			6. Salir
    			Elija una opcion:""");
	}
	private boolean ejecutarOpciones(Scanner consola){
		var opcion = Integer.parseInt(consola.nextLine());
		var salir = false;
		switch (opcion){
			case 1 -> {//Listar estudiantes
				logger.info(nl+"listado de estudiantes: "+nl);
				List<Estudiantes2022> estudiantes = estudianteServicio.listarEstudiantes();
				estudiantes.forEach((estudiante -> logger.info(estudiante.toString()+nl)));
			}
			case 2 ->{//buscar estudiante por id
				logger.info("Digite el id estudiante a buscar: ");
				var idEstudiante = Integer.parseInt(consola.nextLine());
				Estudiantes2022 estudiante =
						estudianteServicio.buscarEstudiantePorId(idEstudiante);
				if(estudiante != null)
					logger.info("Estudiante encontrado: "+estudiante+nl);
				else
					logger.info("Estudiante NO encontrado: "+estudiante+nl);
			}
			case 3 ->{//Agregar esdtudiante
				logger.info("Agregar estudiante: "+nl);
				logger.info("Nombre: ");
				var nombre = consola.nextLine();
				logger.info("Apellido: ");
				var apellido = consola.next();
				logger.info("Telefono: ");
				var telefono = consola.next();
				logger.info("Email: ");
				var email = consola.next();
				//crear el objeto estudiante sin el id
				var estudiante = new Estudiantes2022();
				estudiante.setNombre(nombre);
				estudiante.setApellido(apellido);
				estudiante.setTelefono(telefono);
				estudiante.setEmail(email);
				estudianteServicio.guardarEstudiante(estudiante);
				logger.info("Estudiante agregado:"+estudiante+nl);
			}
			case 4 ->{//modificar estudiante
				logger.info("modificar estudiante: "+nl);
				logger.info("ingrese el id estudiante: ");
				var idEstudiante  = Integer.parseInt(consola.nextLine());
				//buscamos estudainte a modificar
				Estudiantes2022 estudiante =
						estudianteServicio.buscarEstudiantePorId(idEstudiante);
				if(estudiante != null){
					logger.info("Nombre: ");
					var nombre = consola.nextLine();
					logger.info("Apellido: ");
					var apellido = consola.next();
					logger.info("Telefono: ");
					var telefono = consola.next();
					logger.info("Email: ");
					var email = consola.next();
					estudiante.setNombre(nombre);
					estudiante.setApellido(apellido);
					estudiante.setTelefono(telefono);
					estudiante.setEmail(email);
					estudianteServicio.guardarEstudiante(estudiante);
					logger.info("Estudiante modificado:"+estudiante+nl);
				}
				else
					logger.info("Estudiante NO encontrado con el id: "+idEstudiante+nl);
			}
			case 5->{//eliminar estudiante
				logger.info("Eliminar estudiante: "+nl);
				logger.info("ingrese el id estudiante: ");
				var idEstudiante  = Integer.parseInt(consola.nextLine());
				//buscamos el id del estudiante a eliminar
				var estudiante = estudianteServicio.buscarEstudiantePorId(idEstudiante);
				if(estudiante != null){
					estudianteServicio.eliminarEstudiante(estudiante);
					logger.info("Estudiante eliminado: "+estudiante+nl);
				}
				else
					logger.info("Estudiante NO encontrado con el id: "+idEstudiante+nl);
			}
			case 6 ->{//salir
				logger.info("hasta pronto!"+nl+nl);
				salir = true;
			}
			default -> logger.info("opcion incorrecta: "+opcion+nl);
		}//fin switch
		return salir;
	}//Fin metodo ejecutarOpciones

}//Fin clase EstudianteAplication

