# Registry-Root

Root directory content of the Khronos Registry (at khronos.org/registry/).
Includes redirects for the old, pre-Github setup of the registry in
.htaccess.
Each API registry is maintained in a separate Github repository.

On the Khronos webserver, clones of these independent registries are located
as immediate subdirectories of the root repository clone.
They are renamed for brevity, e.g. Github repository
KhronosGroup/OpenGL-Registry is kept in a local clone directory named just
'OpenGL'.
This general pattern is followed with a couple of exceptions
(Vulkan-Web-Registry -> vulkan, for example).

This repository rarely require updates. Its contents are little more than
the toplevel registry index page, the Khronos Implementer's Guide, and the
.htaccess redirects.
If it does need updates, they can be proposed at pull requests to the
www.github.com/KhronosGroup/Registry-Root repository.
