<?php
$static_title = 'Khronos Registry';

include_once("../assets/static_pages/khr_page_top.php");
?>

<p> The Khronos registry contains specifications, header files,
    extension specifications, enumerant and function registries, and
    other related documentation for Khronos APIs, Languages, and related
    products. </p>

<p> The Khronos API Implementers Guide, available in
    <a href="implementers_guide.html"> HTML </a> and
    <a href="implementers_guide.pdf"> PDF </a> versions, provides
    guidelines for implementers of OpenGL ES, OpenVG and other API
    standards specified by the Khronos Group. The aim of these hints is
    to provide commonality between implementations to ease the
    logistical problems faced by developers using multiple different
    implementations of an API. One of the primary goals is to allow an
    application binary to run on top of multiple different OpenGL ES /
    OpenVG / EGL implementations on the same platform. Implementers are
    strongly urged to comply with these guidelines. </p>

<p> The registry is broken down into separate sections for each API.
    These sections include: </p>

<ul>
<li> <a href="https://www.khronos.org/collada/wiki/Portal:Extensions_directory">
     COLLADA&trade; Registry </a>
<li> <a href="DataFormat/"> Data Format Registry </a> </li>
<li> <a href="EGL/"> EGL&trade; Registry </a> </li>
<li> <a href="NNEF/"> NNEF&trade; Registry </a> </li>
<li> <a href="OpenCL/"> OpenCL&trade; Registry </a> </li>
<li> <a href="OpenGL/"> Combined OpenGL&reg;, OpenGL ES, and OpenGL SC Registry </a> </li> </li>
<li> <a href="OpenKODE/"> OpenKODE Registry </a> </li>
<li> <a href="OpenMAX-AL/"> OpenMAX&trade; AL Registry </a> </li>
<li> <a href="OpenMAX-DL/"> OpenMAX DL Registry </a> </li>
<li> <a href="OpenMAX-IL/"> OpenMAX IL Registry </a> </li>
<li> <a href="OpenSL-ES/"> OpenSL ES&trade; Registry </a> </li>
<li> <a href="OpenVG/"> OpenVG&trade; Registry </a> </li>
<li> <a href="OpenVX/"> OpenVX&trade; Registry </a> </li>
<li> <a href="OpenWF/"> OpenWF Registry </a> </li>
<li> <a href="SPIR/"> SPIR&trade; Registry </a> </li>
<li> <a href="spir-v/"> SPIR-V Registry </a> </li>
<li> <a href="SYCL/"> SYCL&trade; Registry </a> </li>
<li> <a href="vulkan/"> Vulkan&reg; Registry </a> </li>
<li> <p> <a href="webgl/"> WebGL&trade; Registry </a>
     (<b>Note:</b> the related TypedArray Registry defined functionality
     that is now part of the <a
     href="http://www.ecma-international.org/ecma-262/6.0/#sec-typedarray-objects">
     ECMAScript 2015 Language Specification</a>, and has been removed from
     the Khronos website. Links to that registry now redirect to the
     corresponding section of the ECMAScript Specification.) </p> </li>
<li> <a href="webcl/"> WebCL&trade; Registry </a>
</ul>

<h3> <a name="headers"></a>
     Collected Khronos Header Files </h3>

<p> <b> As of March 2017, we are no longer providing a single package
    containing collected header files. </b> This package was usually long
    out of date in any event, and the individual APIs publish header files
    in their respective registry pages, or in github repositories linked
    from those pages. Normally header files are shipped as part of SDK
    and/or driver packages provided by operating system and/or hardware
    vendors. </p>

<p> Note that if you download individual header files, several of the
    APIs depend on the shared header file
    <a href="EGL/api/KHR/khrplatform.h"> &lt;KHR/khrplatform.h&gt; </a>,
    which defines common datatypes and calling convention macros. </p>

<?php include_once("../assets/static_pages/khr_page_bottom.php"); ?>
</body>
</html>
