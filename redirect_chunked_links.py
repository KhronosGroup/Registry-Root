#!/usr/bin/python3
#
# Copyright 2024 The Khronos Group Inc.
# SPDX-License-Identifier: Apache-2.0

# redirect_chunked_links.py - generate Apache .htaccess to redirect chapters
# of the chunked spec to corresponding pages the Vulkan documentation site,
# docs.vulkan.org
#
# Relies on the only '<h2' element of each page containing an id attribute
# mapping to a docs page.

# Usage: redirect_chunked_links -basedir path chapter-file [chapter-file...]
# -basedir is the directory containing the cloned vulkan registry
# chapter-file is an individual chapter of the chunked spec (multiple
#   versions can be included) under basedir
# Output is a list of .htaccess directives rewriting the chapter-files to
# the docs site.

# How to get useful output:
# Vulkan-Web-Registry clone must be under directory '$reg/vulkan'
# where 'reg' is a local path
#
# redirect_chunked_links.py -basedir $reg $reg/vulkan/specs/*/html/chap*.html

# This relies on a static map from the 'id' attributes of chunked files
# (which are the anchor names of each chapter) to the docs site.
# While it is possible to extract the anchors directly from the .adoc files -
# the Antora conversion script does this - we don't require that complexity.
# If the chapters are renamed at some point, the static map will need to be
# updated and the rewrite directive regenerated.

# Map from id attributes to Antora filenames
chapterMap = {
    'private-data':                'spec/latest/chapters/VK_EXT_private_data.html',
    'memory-decompression':        'spec/latest/chapters/VK_NV_memory_decompression.html',
    'acceleration-structure':      'spec/latest/chapters/accelstructures.html',
    'boilerplate':                 'spec/latest/appendices/boilerplate.html',
    'capabilities':                'spec/latest/chapters/capabilities.html',
    'clears':                      'spec/latest/chapters/clears.html',
    'cluster-culling':             'spec/latest/chapters/VK_HUAWEI_cluster_culling_shader/clusterculling.html',
    'commandbuffers':              'spec/latest/chapters/cmdbuffers.html',
    'compressed_image_formats':    'spec/latest/appendices/compressedtex.html',
    'copies':                      'spec/latest/chapters/copies.html',
    'credits':                     'spec/latest/appendices/credits.html',
    'debugging':                   'spec/latest/chapters/debugging.html',
    'deferred-host-operations':    'spec/latest/chapters/VK_KHR_deferred_host_operations/deferred_host_operations.html',
    'descriptorsets':              'spec/latest/chapters/descriptorsets.html',
    'devsandqueues':               'spec/latest/chapters/devsandqueues.html',
    'dispatch':                    'spec/latest/chapters/dispatch.html',
    'drawing':                     'spec/latest/chapters/drawing.html',
    'executiongraphs':             'spec/latest/chapters/executiongraphs.html',
    'extendingvulkan':             'spec/latest/appendices/extensions.html',
    'extensions':                  'spec/latest/chapters/extensions.html',
    'features':                    'spec/latest/chapters/features.html',
    'formats':                     'spec/latest/chapters/formats.html',
    'fragmentdensitymapops':       'spec/latest/chapters/fragmentdensitymapops.html',
    'fragops':                     'spec/latest/chapters/fragops.html',
    'framebuffer':                 'spec/latest/chapters/framebuffer.html',
    'fundamentals':                'spec/latest/chapters/fundamentals.html',
    'fxvertex':                    'spec/latest/chapters/fxvertex.html',
    'device-generated-commands':   'spec/latest/chapters/VK_NV_device_generated_commands/generatedcommands.html',
    'geometry':                    'spec/latest/chapters/geometry.html',
    'lexicon':                     'spec/latest/appendices/glossary.html',
    'initialization':              'spec/latest/chapters/initialization.html',
    'interfaces':                  'spec/latest/chapters/interfaces.html',
    'introduction':                'spec/latest/chapters/introduction.html',
    'invariance':                  'spec/latest/appendices/invariance.html',
    'limits':                      'spec/latest/chapters/limits.html',
    'low-latency2':                'spec/latest/chapters/VK_NV_low_latency2/low_latency2.html',
    'memory':                      'spec/latest/chapters/memory.html',
    'memory-model':                'spec/latest/appendices/memorymodel.html',
    'mesh':                        'spec/latest/chapters/VK_NV_mesh_shader/mesh.html',
    'micromap':                    'spec/latest/chapters/VK_EXT_opacity_micromap/micromaps.html',
    'opticalflow':                 'spec/latest/chapters/VK_NV_optical_flow/optical_flow.html',
    'pipelines':                   'spec/latest/chapters/pipelines.html',
    'preamble':                    'spec/latest/chapters/preamble.html',
    'primsrast':                   'spec/latest/chapters/primsrast.html',
    'queries':                     'spec/latest/chapters/queries.html',
    'ray-tracing':                 'spec/latest/chapters/raytracing.html',
    'ray-traversal':               'spec/latest/chapters/raytraversal.html',
    'renderpass':                  'spec/latest/chapters/renderpass.html',
    'resources':                   'spec/latest/chapters/resources.html',
    'roadmap':                     'spec/latest/appendices/roadmap.html',
    'samplers':                    'spec/latest/chapters/samplers.html',
    'shaders':                     'spec/latest/chapters/shaders.html',
    'sparsememory':                'spec/latest/chapters/sparsemem.html',
    'spirvenv':                    'spec/latest/appendices/spirvenv.html',
    'synchronization':             'spec/latest/chapters/synchronization.html',
    'tessellation':                'spec/latest/chapters/tessellation.html',
    'textures':                    'spec/latest/chapters/textures.html',
    'versions':                    'spec/latest/appendices/versions.html',
    'vertexpostproc':              'spec/latest/chapters/vertexpostproc.html',
    'video-coding':                'spec/latest/chapters/videocoding.html',
    'wsi':                         'spec/latest/chapters/VK_KHR_surface/wsi.html',
}

import argparse
import os
import sys
from lxml import etree

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-basedir', action='store',
                        required=True,
                        help='Path to directory containing Vulkan registry files')
    parser.add_argument('files', metavar='filename', nargs='*',
                        help='Path to a chunked HTML output file in the registry')
    args = parser.parse_args()

    # URL to the documentation site
    docsURL = 'https://docs.vulkan.org'

    # Normalize base directory
    absbasepath = os.path.abspath(args.basedir)

    errCount = 0
    for chunkpath in args.files:
        parser = etree.HTMLParser()
        tree = etree.parse(chunkpath, parser)

        # Find the first 'h2' element
        h2elem = tree.find('.//h2')

        if h2elem is None:
            print(f'Cannot find <h2> element for {chunkpath}, not remapped', file=sys.stderr)
            errCount += 1
            continue

        id = h2elem.get('id')
        if id is None:
            print(f'Cannot find id attribute for <h2> element for {chunkpath}, not remapped', file=sys.stderr)
            errCount += 1
            continue

        if id not in chapterMap:
            print(f'Cannot map id attribute {id} for <h2> element for {chunkpath}, not remapped', file=sys.stderr)
            errCount += 1
            continue

        # Normalize chunk path
        abschunkpath = os.path.abspath(chunkpath)

        # Find chunk path relative to basedir
        relchunkpath = os.path.relpath(abschunkpath, absbasepath)

        remapPath = docsURL + '/' + chapterMap[id]

        print(f'Redirect 301 /{relchunkpath} {remapPath}')

    if errCount > 0:
        print(f'{errCount} files failed')
        sys.exit(1)
