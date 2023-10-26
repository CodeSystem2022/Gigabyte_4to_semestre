package utn.tienda_libros.vista;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import utn.tienda_libros.servicio.LibroServicio;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;

@Component
public class LibroFrom extends JFrame {
    LibroServicio libroServicio;
    private JPanel panel;
    private JTable tablaLibros;
    private DefaultTableModel tablaModeloLibros;

    @Autowired
    public LibroFrom(LibroServicio libroServicio) {
        this.libroServicio = libroServicio;
        iniciarForma();
    }

    private void iniciarForma(){


        setContentPane(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setSize(900, 700);

        //Para obtener las dimensiones de la ventana

        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = toolkit.getScreenSize();
        int x = (tamanioPantalla.width - getWidth() / 2);
        int y = (tamanioPantalla.height - getHeight() / 2);
        setLocation(x, y);

    }

    private void createUIComponents(){
        this.tablaModeloLibros = new DefaultTableModel(0, 5);
        String[] cabecera = {"id", "Libro", "Autor", "Precio", "Existencias"};
        this.tablaModeloLibros.setColumnIdentifiers(cabecera);

        //instanciar el objeto

        this.tablaLibros = new JTable(tablaModeloLibros);

        listarLibros();


    }
    private void listarLibros() {
        //limpiar tabla
        tablaModeloLibros.setRowCount(0);
        /* obtener los libros de la BD */
        var libros = libroServicio.ListarLibros();
        // iteramos cada libro
        libros.forEach((libro)-> {//función lambda
            Object [] renglonLibro = {
                    libro.getIdLibro(),
                    libro.getNombreLibro(),
                    libro.getAutor(),
                    libro.getPrecio(),
                    libro.getExistencias(),


            };
            this.tablaModeloLibros.addRow(renglonLibro);
        });


    };
}
