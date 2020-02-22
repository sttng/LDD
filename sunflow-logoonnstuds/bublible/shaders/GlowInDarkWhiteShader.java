package bublible.shaders;

import org.sunflow.core.shader.ConstantShader;
import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.image.Color;

// mat329
public final class GlowInDarkWhiteShader implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, ok = false;
    Color c = new Color("fbfaec");

    private final String n1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    final PlasticShader $n1 = new PlasticShader();
    private final String n2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    final ConstantShader $n2 = new ConstantShader();

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {

            // one shot
            ok = true;

            // PLASTIC
            api.parameter("color", c);
            b1 = $n1.update(pl, api);
            pl.clear(true);

            // CONSTANT
            api.parameter("color", c.mul(1.2f));
            b2 = $n2.update(pl, api);
            pl.clear(true);

            return (b1 && b2);
        }
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getRadiance(ShadingState state) {
        Color p = $n1.getRadiance(state);
        Color cs = $n2.getRadiance(state);
        Color rColor = Color.blend(p, cs, 0.15f);
        return rColor;
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
