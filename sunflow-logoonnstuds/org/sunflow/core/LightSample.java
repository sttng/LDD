package org.sunflow.core;

import bublible.shaders.NeonShader;
import bublible.shaders.TransparentShader;
import java.util.HashMap;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.image.Color;
import org.sunflow.math.Vector3;

/**
 * Represents a sample taken from a light source that faces a point being
 * shaded.
 */
public class LightSample {

    private Ray shadowRay; // ray to be used to evaluate if the point is in
    // shadow
    private Color ldiff;
    private Color lspec;
    LightSample next; // pointer to next item in a linked list of samples
    private Color shadowcolor;

    /**
     * Creates a new light sample object (invalid by default).
     */
    public LightSample() {
        ldiff = lspec = null;
        shadowRay = null;
        next = null;
    }

    boolean isValid() {
        return ldiff != null && lspec != null && shadowRay != null;
    }

    /**
     * Set the current shadow ray. The ray's direction is used as the sample's
     * orientation.
     *
     * @param shadowRay shadow ray from the point being shaded towards the light
     */
    public void setShadowRay(Ray shadowRay) {
        this.shadowRay = shadowRay;
    }

    /**
     * Trace the shadow ray, attenuating the sample's color by the opacity of
     * intersected objects. If the intersected object has trans color then the
     * shadow color will have its colorization.
     *
     * @param state shading state representing the point to be shaded
     */
    public final void traceShadow(ShadingState state) {
        HashMap opacityMap = state.getObjectCastingShadow(shadowRay);
        Color opacity = (opacityMap.get("hit") == "yes") ? Color.WHITE : Color.BLACK;

        if ((Shader) opacityMap.get("shader") instanceof TransparentShader) {
            //ldiff = lspec = state.traceTransparency();
            //Color.blend(ldiff, ldiff, opacity, ldiff);
            //Color.blend(lspec, lspec, opacity, lspec);
        } else {
            try {
                if (((Shader) opacityMap.get("shader") instanceof GlassShader) || ((Shader) opacityMap.get("shader") instanceof NeonShader)) {
                    shadowcolor = new Color((Color) opacityMap.get("color"));
                    Color.blend(shadowcolor, Color.BLACK, (1.0f - ldiff.r) + 0.03f, shadowcolor);
                } else {
                    shadowcolor = Color.BLACK;
                }
            } catch (UnsupportedOperationException e) {
                shadowcolor = Color.BLACK;
            } catch (Exception e) {
                //e.printStackTrace();
                shadowcolor = Color.BLACK;
            }

            Color.blend(ldiff, shadowcolor, opacity, ldiff);
            Color.blend(lspec, shadowcolor, opacity, lspec);
        }
    }

    /**
     * Get the sample's shadow ray.
     *
     * @return shadow ray
     */
    public Ray getShadowRay() {
        return shadowRay;
    }

    /**
     * Get diffuse radiance.
     *
     * @return diffuse radiance
     */
    public Color getDiffuseRadiance() {
        return ldiff;
    }

    /**
     * Get specular radiance.
     *
     * @return specular radiance
     */
    public Color getSpecularRadiance() {
        return lspec;
    }

    /**
     * Set the diffuse and specular radiance emitted by the current light
     * source. These should usually be the same, but are distinguished to allow
     * for non-physical light setups or light source types which compute diffuse
     * and specular responses seperately.
     *
     * @param d diffuse radiance
     * @param s specular radiance
     */
    public void setRadiance(Color d, Color s) {
        ldiff = d.copy();
        lspec = s.copy();
    }

    /**
     * Compute a dot product between the current shadow ray direction and the
     * specified vector.
     *
     * @param v direction vector
     * @return dot product of the vector with the shadow ray direction
     */
    public float dot(Vector3 v) {
        return shadowRay.dot(v);
    }
}
