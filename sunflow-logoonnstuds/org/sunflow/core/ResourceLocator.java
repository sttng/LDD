package org.sunflow.core;

import java.io.InputStream;

public interface ResourceLocator {
    InputStream getResource(String name);
}