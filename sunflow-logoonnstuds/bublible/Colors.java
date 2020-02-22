package bublible;

import org.sunflow.image.Color;

// Additional shader functions
public class Colors extends Color {

    // Makes bricks looking kind-of old/discolored
    public static final Color bleech(float f, Color c) {
        Color dest = new Color();
        dest.r = c.r + f;
        dest.g = c.g + f;
        dest.b = c.b + f;
        return dest;
    }
}
