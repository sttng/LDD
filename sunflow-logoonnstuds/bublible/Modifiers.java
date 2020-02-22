package bublible;

import java.util.Arrays;
import org.sunflow.SunflowAPI;
import org.sunflow.core.Modifier;
import org.sunflow.core.modifiers.BumpMappingModifier;
import org.sunflow.core.parser.SCParser;

// Additional shader functions
public class Modifiers {

    private static Utils q;
    private final Bricks m = new Bricks();

    /**
     * Return mixture color output between color and texture.
     *
     * @param api
     * @param gs_strength
     * @param bp_strength
     */
    public void Grains(SunflowAPI api, float gs_strength, float bp_strength) {
        String[] brick = m.checkGrainySlopes();
        for (String a : brick) {
            float b = gs_strength;
            String c = "Slopes" + a;
            if (SCParser.exactdecorbp.equals("on")) {
                if (Arrays.asList(m.checkGrainyBP32x32()).contains(a)) {
                    a = "BP32x32";
                    b = bp_strength;
                    c = "BP32x32";
                } else if (Arrays.asList(m.checkGrainyBP16x16()).contains(a)) {
                    a = "BP16x16";
                    b = bp_strength;
                    c = "BP16x16";
                }
            }
            String mdfr = "modGrainy" + c;
            Modifier s = api.lookupModifier(mdfr);
            if (s == null) {
                api.parameter("texture", "bublible/img/gs/gs" + a + ".png");
                api.parameter("scale", b);
                api.modifier(mdfr, new BumpMappingModifier());
            }
        }
    }
}
