package bublible.shaders;

import bublible.Shaders;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.image.Color;

// TransparentShader
public final class TransparentShader implements Shader {

    private final Color dacolor = new Color(1.0f, 1.0f, 1.0f);

    public TransparentShader() {
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        return true;
    }

    public Color getMaterialColor() {
        return dacolor;
    }

    public Color getRadiance(ShadingState state) {
        state.faceforward();
        Color color = state.traceTransparency();
        return Shaders.getMixture(state, color, "glass");
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
