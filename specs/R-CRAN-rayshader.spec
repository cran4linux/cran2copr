%global packname  rayshader
%global packver   0.13.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.2
Release:          1%{?dist}
Summary:          Create Maps and Visualize Data in 2D and 3D

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rayrender 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-png 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-imager 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-CRAN-rayrender 
Requires:         R-methods 

%description
Uses a combination of raytracing and multiple hill shading methods to
produce 2D and 3D data visualizations and maps. Includes water detection
and layering functions, programmable color palette generation, several
built-in textures for hill shading, 2D and 3D plotting options, a built-in
path tracer, 'Wavefront' OBJ file export, and the ability to save 3D
visualizations to a 3D printable format.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
