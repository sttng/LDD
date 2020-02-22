package bublible;

import java.awt.AlphaComposite;
//import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics2D;
import java.awt.font.TextLayout;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;
import java.io.IOException;
import java.util.ArrayList;
import org.sunflow.core.Display;
import org.sunflow.core.parser.SCParser;
import org.sunflow.image.Color;

// Several useful methods
public class Watermark {

    private static final String TXT = "rendered using\n" + Utils.MODNAME + Utils.VERSION + "\nas rendering engine for BR";
    private static final String imageSavePath = "c:/www.png";
    private static Color[] bucketFull;
    private static ArrayList<Object[]> multiArrayList = new ArrayList<>();
    private static final int[] BORDERS = {Color.RED.toRGB(),
        Color.GREEN.toRGB(), Color.BLUE.toRGB(), Color.YELLOW.toRGB(),
        Color.CYAN.toRGB(), Color.MAGENTA.toRGB()};

    public static void setImage(int x, int y, int w, int h, Color[] data) {
        Object[] ob = {x, y, w, h, data};
        multiArrayList.add(ob);
    }

    /**
     * Embeds a textual watermark over a source image.
     *
     * @param width source image width
     * @param height source image height
     * @param display window where output image is painted
     * @param renderThreads
     * @throws java.io.IOException
     */
    public static void addText(int width, int height, Display display, Thread[] renderThreads) throws IOException {

        if (SCParser.credentials.equals("on")) {

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
                        //sourceImage.setRGB(x + i, y + j, data[index].toRGB());
                    }
                }
            }

            Graphics2D g2d = (Graphics2D) sourceImage.getGraphics();
            //g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

            // initializes necessary graphic properties
            AlphaComposite alphaChannel = AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 1f);
            g2d.setComposite(alphaChannel);
            FontMetrics fontMetrics = g2d.getFontMetrics();

            //Effect glow = new Glow(1.0);
            //text.setEffect(glow);
            // calculates the coordinate where the String is painted
            int centerX = width;
            int centerY = height - 50;

            /*g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
             FontRenderContext frc = g2d.getFontRenderContext();
             Font font = new Font("lucida sans demibold", Font.PLAIN, 48);
             g2d.setFont(font);
             TextLayout textLayout = new TextLayout(TXT, font, frc);
             Rectangle2D r2 = textLayout.getBounds();
             float scale = 1.25f;
             double x = (width - scale*r2.getWidth())/2;
             double y = (height + scale*r2.getHeight())/2;
             AffineTransform at = AffineTransform.getTranslateInstance(x,y);
             at.scale(scale, scale);
             Shape outline = textLayout.getOutline(at);
             Rectangle r = outline.getBounds();
             float x1 = r.x + r.width/2;
             float y1 = r.y + r.height/2;
             float y2 = height*5/8;
             GradientPaint gradient = new GradientPaint(x1, y1, java.awt.Color.RED, x1, y2, java.awt.Color.YELLOW, true);
             g2d.setPaint(gradient);
             g2d.fill(outline);*/
            
            /*Group rootGroup = new Group();
            Scene scene = new Scene(rootGroup, 800, 400);
            Text text1 = new Text(25, 25, "java2s.com");
            text1.setFill(Color.CHOCOLATE);
            text1.setFont(Font.font(java.awt.Font.MONOSPACED, 35));
            Effect glow = new Glow(1.0);
            text1.setEffect(glow);
            rootGroup.getChildren().add(text1);
            stage.setScene(scene);
            stage.show();*/
            
            /*//blur the shadow: result is sorted in image2
             float ninth = 1.0f / 9.0f;
             float[] kernel = {ninth, ninth, ninth, ninth, ninth, ninth, ninth, ninth, ninth};
             ConvolveOp op = new ConvolveOp(new Kernel(3, 3, kernel), ConvolveOp.EDGE_NO_OP, null);
             BufferedImage image2 = op.filter(image, null);*/
            
            /*int x = 10;
            int y = 100;
            Font font = new Font("Georgia", Font.ITALIC, 50);
            TextLayout textLayout = new TextLayout(TXT, font, g2d.getFontRenderContext());
            g2d.setPaint(new java.awt.Color(150, 150, 150));
            textLayout.draw(g2d, x + 3, y + 3);
            g2d.setPaint(java.awt.Color.BLACK);
            textLayout.draw(g2d, x, y);*/
            
            // paints the textual watermark
            //drawString(g2d, text, centerX + 6, centerY + 1, sourceImage.getWidth(), "shadow");
            drawString(g2d, centerX, centerY, sourceImage.getWidth(), "popis");

            //ImageIO.write(sourceImage, "png", new File(imageSavePath));
            g2d.dispose();
            
            // BufferedImage to Color array
            int[] dt = ((DataBufferInt) sourceImage.getRaster().getDataBuffer()).getData();

            bucketFull = new Color[dt.length];
            for (int i = 0; i < dt.length; i++) {
                bucketFull[i] = new Color(dt[i]).toLinear();
            }

            // update and repaint output image
            display.imagePrepare(0, 0, width, height, renderThreads.length + 1);
            display.imageUpdate(0, 0, width, height, bucketFull);

            // reset objects
            g2d = null;
            sourceImage = null;
            bucketFull = null;
            multiArrayList = new ArrayList<>();
        }
    }

    private static void drawString(Graphics2D g, int x, int y, int total_width, String c) {
        int q = 3;
        for (String line : TXT.split("\n")) {
            /*Font currentFont = g.getFont();
             Font newFont = currentFont.deriveFont(currentFont.getSize() * 1.4f);
             g.setFont(newFont);*/
            java.awt.Color colA, colB;
            if (c.equals("shadow")) {
                colA = colB = new java.awt.Color(150, 150, 150);
            } else {
                colA = new java.awt.Color(255, 0, 0);
                colB = new java.awt.Color(0, 0, 0);
            }

            if (q == 4) {
                g.setColor(colA);
                g.setFont(new Font("Arial", Font.BOLD, 11));
            } else {
                g.setColor(colB);
                g.setFont(new Font("Arial", Font.PLAIN, 9));
            }
            int padding = 10;
            int actual_width = g.getFontMetrics().stringWidth(line);
            int ix = total_width - actual_width - padding;
            g.drawString(line, ix, y += g.getFontMetrics().getHeight());

            q++;
        }
    }

    private static int ShiftNorth(int p, int distance) {
        return (p - distance);
    }

    private static int ShiftSouth(int p, int distance) {
        return (p + distance);
    }

    private static int ShiftEast(int p, int distance) {
        return (p + distance);
    }

    private static int ShiftWest(int p, int distance) {
        return (p - distance);
    }
}
