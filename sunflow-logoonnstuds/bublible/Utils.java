package bublible;

import b.a.q;
import blueprint.c;
import c.i;
import java.awt.AlphaComposite;
//import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.GradientPaint;
import java.awt.Graphics2D;
import java.awt.Paint;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import javax.imageio.ImageIO;
import org.sunflow.core.Display;
import org.sunflow.core.parser.SCParser;
import org.sunflow.image.Color;

// Several useful methods
public class Utils {

    private static final String delA = ",";
    private static final String delB = "_";
    private static int stav = 0;
    public static final String MODNAME = "bublible's SunFlow MOD v";
    public static final String VERSION = "20160717";
    public static final String INFO = "Rendered using " + MODNAME + VERSION;
    public static final String COPYRIGHT = "2015-" + Calendar.getInstance().get(Calendar.YEAR) + ", Milos Plank";
    public static final String URL = "http://lego.queryen.com/php/_sfmod.php";
    public static ArrayList<Color> bucket = new ArrayList<>();
    public static Color[] bucketFull;
    private static int imageW, imageH;
    private static String imageBucketValues = "";
    private static ArrayList<Object[]> multiArrayList = new ArrayList<>();
    private static final int[] BORDERS = {Color.RED.toRGB(),
        Color.GREEN.toRGB(), Color.BLUE.toRGB(), Color.YELLOW.toRGB(),
        Color.CYAN.toRGB(), Color.MAGENTA.toRGB()};

    public static void setImage(int x, int y, int w, int h, Color[] data) {
        Object[] ob = {x, y, w, h, data};
        multiArrayList.add(ob);
    }

    public static void setImageDimensions(int w, int h) {
        imageW = w;
        imageH = h;
    }

    public static void setImageBucketValues(Color rgb) {
        imageBucketValues += rgb.toString() + "_";
    }

    /**
     * Some quick "Short & Easy" output to CMD window.
     *
     * @param s string to be send to CMD window as output
     * @throws java.io.FileNotFoundException
     */
    public static void w(String s) throws FileNotFoundException {
        if (stav == 0) {
            if (SCParser.checkAttributeStatus("cmdtolog").equals("on")) {
                System.setOut(new PrintStream(new FileOutputStream("cmd.log")));
            }
            stav++;
        }
        System.out.println(s);
    }

    /**
     * Iterate thru a Map.
     *
     * @param mp map to be interated
     * @return string of
     */
    public static String printMap(Map mp) {
        String s = new String();
        Iterator it = mp.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry) it.next();
            s += pair.getKey() + "=" + pair.getValue() + delA;
            //it.remove();
        }
        return s;
    }

    /**
     * Prepares all brick info for CMD output.
     *
     * @param s string to be send to CMD window as o
     * @throws java.io.FileNotFoundException
     */
    public static void bricksToCMD(List<String> s) throws FileNotFoundException {

        HashMap<String, String> map = new HashMap<>();
        String output, geometries, brick, sep, instances, nul, br, q, sp, g, tM, bvt, brickname, V, T;
        int velkost, loop;

        V = "VERTICES";
        T = "TRIANGLES";
        tM = "MESH ";
        sep = "--------------------------------------------------------------";
        sp = ":::";
        br = "\r\n";
        q = delB + "name" + delB;
        nul = "";
        output = nul;
        instances = nul;
        geometries = nul;
        velkost = s.size();

        for (String i : s) {
            String[] j = i.split(sp);
            brick = j[0];

            // picking all brick geometries
            if (!geometries.contains(brick)) {
                brickname = brick.split(delB)[0];
                if (!brick.contains(q) && brick.contains(delB + "0")) {
                    geometries += brick + delA;
                    for (String n : s) {
                        String[] p = n.split(sp);
                        if (p[0].equals(brick)) {
                            if (p[1].equals(V)) {
                                map.put(brickname + sp + V, p[2]);
                            } else if (p[1].equals(T)) {
                                map.put(brickname + sp + T, p[2]);
                            }
                        }
                    }
                }
            }

            // picking all brick instances
            if (!instances.contains(brick)) {
                if (brick.contains(q + "0")) {
                    instances += brick + delA;
                    output += sep + br;
                    g = nul;
                    bvt = nul;
                    loop = 0;
                    String sub = nul;
                    for (String k : s) {
                        loop++;
                        String[] m = k.split(sp);
                        if (m[0].equals(brick)) {
                            if (m[1].equals("GEOMETRY")) {
                                g = m[2].split(delB)[0];
                                sub = "BRICK: " + g + br + sub;
                            }
                            if (!m[1].equals("BRICK") && !m[1].equals(V) && !m[1].equals(T)) {
                                if (!m[1].equals("GEOMETRY")) {
                                    sub += m[1] + ": " + m[2] + br;
                                }
                            }
                        }
                        if (loop == velkost) {
                            String[] vt = printMap(map).split(delA);
                            for (String r : vt) {
                                String[] tmpA = r.split(sp);
                                if (tmpA[0].contains(g)) {
                                    String[] tmpB = tmpA[1].split("=");
                                    bvt += tM + tmpB[0] + ": " + tmpB[1] + br;
                                }
                            }
                            sub += bvt;
                            bvt = nul;
                        }
                    }
                    output += sub;
                }
            }
        }
        w(output);
    }

    public static int rndRng(int min, int max) {
        int range = (max - min) + 1;
        return (int) (Math.random() * range) + min;
    }

    public static float clamp(float val, float min, float max) {
        return Math.max(min, Math.min(max, val));
    }

    public static void Copyright() {

        for (int i = 0; i < 300; i++) {
            System.out.println(" ");
        }

        System.out.println("*******************************************************************");
        System.out.println(INFO + " as rendering engine");
        System.out.println("*******************************************************************");
        System.out.println("(C) " + COPYRIGHT);
        System.out.println(URL);

        for (int i = 0; i < 2; i++) {
            System.out.println(" ");
        }
    }

    /**
     * Embeds a textual watermark over a source image to produce a watermarked
     * one.
     *
     * @param sourceImage original rendered image
     * @return
     * @throws java.io.IOException
     */
    public static BufferedImage addTextWatermark(BufferedImage sourceImage) throws IOException {
        //blueprint.a.b.a.b str = new blueprint.a();
        //System.out.println("BlueRender: " + a.a.a.b);
        if (SCParser.credentials.equals("on")) {
            String imageSavePath = "c:/www.png";
            String text = "rendered using\n" + MODNAME + VERSION + "\n\u00a9 " + COPYRIGHT;
            Graphics2D g2d = (Graphics2D) sourceImage.getGraphics();

            // initializes necessary graphic properties
            AlphaComposite alphaChannel = AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.3f);
            g2d.setComposite(alphaChannel);
            //g2d.setColor(Color.RED);
            //g2d.setFont(new Font("Arial", Font.BOLD, 10));
            FontMetrics fontMetrics = g2d.getFontMetrics();
            Rectangle2D rect = fontMetrics.getStringBounds(text, g2d);

            // calculates the coordinate where the String is painted
            //int centerX = (sourceImage.getWidth() - (int) rect.getWidth()) / 2;
            //int centerY = sourceImage.getHeight() / 2;
            int centerX = sourceImage.getWidth();
            int centerY = sourceImage.getHeight() - 50;

            // paints the textual watermark
            //g2d.drawString(text, centerX, centerY);
            drawString(g2d, text, centerX, centerY, sourceImage.getWidth());

            ImageIO.write(sourceImage, "png", new File(imageSavePath));
            g2d.dispose();
        }

        //System.out.println("The tex watermark is added to the image.");
        return sourceImage;
    }

    /**
     * Embeds a textual watermark over a source image to produce a watermarked
     * one.
     *
     * @param width
     * @param height
     * @return
     * @throws java.io.IOException
     */
    public static Color[] addTextWatermarkStream(int width, int height) throws IOException {

        BufferedImage sourceImage = new BufferedImage(width + 58, height + 58, BufferedImage.TYPE_INT_RGB);
        for (int k = 0; k < multiArrayList.size(); k++) {

            // PREPARE...
            int x = (int) multiArrayList.get(k)[0];
            int y = (int) multiArrayList.get(k)[1];
            int w = (int) multiArrayList.get(k)[2];
            int h = (int) multiArrayList.get(k)[3];
            Color[] data = (Color[]) multiArrayList.get(k)[4];
            int border = BORDERS[k % BORDERS.length];

            for (int by = 0; by < h; by++) {
                for (int bx = 0; bx < w; bx++) {
                    if (bx == 0 || bx == w - 1) {
                        if (5 * by < h || 5 * (h - by - 1) < h) {
                            sourceImage.setRGB(x + bx, y + by, border);
                        }
                    } else if (by == 0 || by == h - 1) {
                        if (5 * bx < w || 5 * (w - bx - 1) < w) {
                            sourceImage.setRGB(x + bx, y + by, border);
                        }
                    }
                }
            }

            // UPDATE...
            for (int j = 0, index = 0; j < h; j++) {
                for (int i = 0; i < w; i++, index++) {
                    sourceImage.setRGB(x + i, y + j, data[index].copy().toNonLinear().toRGB());
                }
            }
        }

        if (SCParser.credentials.equals("on")) {

            String imageSavePath = "c:/www.png";
            String text = "rendered using\n" + MODNAME + VERSION + "\n\u00a9 " + COPYRIGHT;
            Graphics2D g2d = (Graphics2D) sourceImage.getGraphics();

            // initializes necessary graphic properties
            AlphaComposite alphaChannel = AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.3f);
            g2d.setComposite(alphaChannel);
            //g2d.setColor(Color.RED);
            FontMetrics fontMetrics = g2d.getFontMetrics();
            Rectangle2D rect = fontMetrics.getStringBounds(text, g2d);

            // calculates the coordinate where the String is painted
            int centerX = sourceImage.getWidth();
            int centerY = sourceImage.getHeight() - 50;

            // paints the textual watermark
            drawString(g2d, text, centerX, centerY, sourceImage.getWidth());

            ImageIO.write(sourceImage, "png", new File(imageSavePath));
            g2d.dispose();

            // Image to Color array
            int[] dt = ((DataBufferInt) sourceImage.getRaster().getDataBuffer()).getData();
            System.out.println("dt.length = " + dt.length);
            bucketFull = new Color[dt.length];
            for (int i = 0; i < dt.length; i++) {
                bucketFull[i] = new Color(dt[i]);
            }
        }

        return bucketFull;
    }

    /**
     * Embeds a textual watermark over a source image to produce a watermarked
     * one.
     *
     * @param width
     * @param height
     * @param display
     * @param renderThreads
     * @throws java.io.IOException
     */
    public static void addTextWatermarkStream(int width, int height, Display display, Thread[] renderThreads) throws IOException {

        /*BufferedImage b_img = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
         Graphics2D graphics = b_img.createGraphics();
         graphics.setPaint(new java.awt.Color(0,0,0));
         graphics.fillRect(0, 0, b_img.getWidth(), b_img.getHeight());*/
        BufferedImage sourceImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        for (int k = 0; k < multiArrayList.size(); k++) {

            // PREPARE...
            int x = (int) multiArrayList.get(k)[0];
            int y = (int) multiArrayList.get(k)[1];
            int w = (int) multiArrayList.get(k)[2];
            int h = (int) multiArrayList.get(k)[3];
            Color[] data = (Color[]) multiArrayList.get(k)[4];
            int border = BORDERS[k % BORDERS.length];

            for (int by = 0; by < h; by++) {
                for (int bx = 0; bx < w; bx++) {
                    if (bx == 0 || bx == w - 1) {
                        if (5 * by < h || 5 * (h - by - 1) < h) {
                            sourceImage.setRGB(x + bx, y + by, border);
                        }
                    } else if (by == 0 || by == h - 1) {
                        if (5 * bx < w || 5 * (w - bx - 1) < w) {
                            sourceImage.setRGB(x + bx, y + by, border);
                        }
                    }
                }
            }
            // UPDATE...
            for (int j = 0, index = 0; j < h; j++) {
                for (int i = 0; i < w; i++, index++) {
                    sourceImage.setRGB(x + i, y + j, data[index].copy().toNonLinear().toRGB());
                }
            }
        }

        if (SCParser.credentials.equals("on")) {

            String imageSavePath = "c:/www.png";
            String text = "rendered using\n" + MODNAME + VERSION + "\n\u00a9 " + COPYRIGHT;
            Graphics2D g2d = (Graphics2D) sourceImage.getGraphics();

            // initializes necessary graphic properties
            AlphaComposite alphaChannel = AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.3f);
            g2d.setComposite(alphaChannel);
            g2d.setColor(new java.awt.Color(255, 0, 0));
            FontMetrics fontMetrics = g2d.getFontMetrics();
            Rectangle2D rect = fontMetrics.getStringBounds(text, g2d);

            // calculates the coordinate where the String is painted
            int centerX = width;
            int centerY = height - 60;

            // paints the textual watermark
            drawString(g2d, text, centerX, centerY, sourceImage.getWidth());

            //ImageIO.write(sourceImage, "png", new File(imageSavePath));
            g2d.dispose();

            // Image to Color array
            int[] dt = ((DataBufferInt) sourceImage.getRaster().getDataBuffer()).getData();
            bucketFull = new Color[dt.length];
            for (int i = 0; i < dt.length; i++) {
                bucketFull[i] = new Color(dt[i]);
            }
            display.imagePrepare(0, 0, width, height, renderThreads.length + 1);
            display.imageUpdate(0, 0, width, height, bucketFull);

            g2d = null;
        }

        sourceImage = null;
        bucketFull = null;
        multiArrayList = new ArrayList<>();
    }

    /**
     * Embeds a textual watermark over a source image to produce a watermarked
     * one.
     *
     * @throws java.io.IOException
     */
    public static void addTextWatermark() throws IOException {
        //System.out.println("BlueRender: " + bluerender.b.STYLESHEET_CASPIAN);
        if (SCParser.credentials.equals("on")) {
            String imageSavePath = "c:/www.png";
            String text = "rendered using\n" + MODNAME + VERSION + "\n\u00a9 " + COPYRIGHT;

            BufferedImage sourceImage = ImageIO.read(new File("Z:\\_SERVER_\\root\\www\\_PHP_\\lego\\download\\brmod\\watermark.lxf.png"));
            Graphics2D g2d = (Graphics2D) sourceImage.getGraphics();

            // initializes necessary graphic properties
            AlphaComposite alphaChannel = AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.3f);
            g2d.setComposite(alphaChannel);
            //g2d.setColor(Color.RED);
            //g2d.setFont(new Font("Arial", Font.BOLD, 10));
            FontMetrics fontMetrics = g2d.getFontMetrics();
            Rectangle2D rect = fontMetrics.getStringBounds(text, g2d);

            // calculates the coordinate where the String is painted
            //int centerX = (sourceImage.getWidth() - (int) rect.getWidth()) / 2;
            //int centerY = sourceImage.getHeight() / 2;
            int centerX = sourceImage.getWidth();
            int centerY = sourceImage.getHeight() - 50;

            // paints the textual watermark
            //g2d.drawString(text, centerX, centerY);
            drawString(g2d, text, centerX, centerY, sourceImage.getWidth());

            ImageIO.write(sourceImage, "png", new File(imageSavePath));
            g2d.dispose();
        }

        //System.out.println("The tex watermark is added to the image.");
    }

    private static void drawString(Graphics2D g, String text, int x, int y, int total_width) {
        int q = 3;
        for (String line : text.split("\n")) {
            /*Font currentFont = g.getFont();
             Font newFont = currentFont.deriveFont(currentFont.getSize() * 1.4f);
             g.setFont(newFont);*/
            if (q == 4) {
                g.setFont(new Font("Arial", Font.BOLD, 12));
            } else {
                g.setFont(new Font("Arial", Font.PLAIN, 10));
            }
            int padding = 10;
            int actual_width = g.getFontMetrics().stringWidth(line);
            int ix = total_width - actual_width - padding;
            g.drawString(line, ix, y += g.getFontMetrics().getHeight());
            q++;
        }
    }

    /**
     * Embeds an image watermark over a source image to produce a watermarked
     * one.
     *
     * @param sourceImage
     * @return
     */
    public static BufferedImage addImageWatermark(BufferedImage sourceImage) {
        try {
            BufferedImage watermarkImage = ImageIO.read(new File("c:/w.png"));

            // initializes necessary graphic properties
            Graphics2D g2d = (Graphics2D) sourceImage.getGraphics();
            AlphaComposite alphaChannel = AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.3f);
            g2d.setComposite(alphaChannel);

            // calculates the coordinate where the image is painted
            int topLeftX = (sourceImage.getWidth() - watermarkImage.getWidth()) / 2;
            int topLeftY = (sourceImage.getHeight() - watermarkImage.getHeight()) / 2;

            // paints the image watermark
            g2d.drawImage(watermarkImage, topLeftX, topLeftY, null);

            //ImageIO.write(sourceImage, "png", destImageFile);
            g2d.dispose();

            //System.out.println("The image watermark is added to the image.");
            return sourceImage;

        } catch (IOException ex) {
            System.err.println(ex);
        }
        return null;
    }
}
