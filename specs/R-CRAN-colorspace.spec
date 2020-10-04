%global packname  colorspace
%global packver   1.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Toolbox for Manipulating and Assessing Colors and Palettes

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Carries out mapping between assorted color spaces including RGB, HSV, HLS,
CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB and polar CIELAB. Qualitative,
sequential, and diverging color palettes based on HCL colors are provided
along with corresponding ggplot2 color scales. Color palette choice is
aided by an interactive app (with either a Tcl/Tk or a shiny GUI) and
shiny apps with an HCL color picker and a color vision deficiency
emulator. Plotting functions for displaying and assessing palettes include
color swatches, visualizations of the HCL space, and trajectories in HCL
and/or RGB spectrum. Color manipulation functions include: desaturation,
lightening/darkening, mixing, and simulation of color vision deficiencies
(deutanomaly, protanomaly, tritanomaly).

%prep
%setup -q -c -n %{packname}


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/cvdemulator
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/hclcolorpicker
%doc %{rlibdir}/%{packname}/hclwizard
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
