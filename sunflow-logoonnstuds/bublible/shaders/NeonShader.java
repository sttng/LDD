package bublible.shaders;

import org.sunflow.core.shader.ConstantShader;
import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.image.Color;

public final class NeonShader implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, ok = false;
    Color c;

    private final String n1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    final GlassShader $n1 = new GlassShader();
    private final String n2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    final ConstantShader $n2 = new ConstantShader();

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {

            // one shot
            ok = true;

            c = pl.getColor("color", c);
            pl.clear(true);

            // GLASS
            api.parameter("color", c);
            api.parameter("eta", 1.6f);
            b1 = $n1.update(pl, api);
            pl.clear(true);

            // CONSTANT
            api.parameter("color", c);
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
        Color gs = $n1.getRadiance(state);
        Color cs = $n2.getRadiance(state);
        return Color.blend(gs, cs, 0.065f).mul(1.5f);
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
