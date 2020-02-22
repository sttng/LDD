package org.sunflow.core.shader;

import bublible.Shaders;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.image.Color;

public class ConstantShader implements Shader {

    private Color c;

    public ConstantShader() {
        this.c = Color.WHITE;
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        c = pl.getColor("color", c);
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getRadiance(ShadingState state) {
        return Shaders.getMixture(state, c, "constant");
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
