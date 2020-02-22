package bublible.shaders;

import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.image.Color;

public class LampShader implements Shader {
    private Color c;
    private float p;

    public LampShader() {
        this.c = Color.WHITE;
        this.p = 1f;
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        c = pl.getColor("color", c);
        p = pl.getFloat("power", p);
        return true;
    }
    
    public Color getMaterialColor(){
        return c;
    }

    public Color getRadiance(ShadingState state) {
        return c.mul(p).clamp(0f, 1000000000f);
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