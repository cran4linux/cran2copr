%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cooltools
%global packver   2.33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.33
Release:          1%{?dist}%{?buildtag}
Summary:          Practical Tools for Scientific Computation and Visualisation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-celestial 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-gitcreds 
BuildRequires:    R-CRAN-pak 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-celestial 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pracma 
Requires:         R-utils 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-gitcreds 
Requires:         R-CRAN-pak 

%description
Provides utilities for scientific computation and visualisation, with an
emphasis on applications in physics and astrophysics. Functionality
includes random sampling from spherical and custom distributions,
information and entropy analysis, Fourier transforms, two-point
correlation estimation, binning and gridding of point sets,
two-dimensional interpolation, Monte Carlo integration, vector operations,
coordinate transformations, physical constants, and cosmological
conversions. Graphics tools support the creation and export of
publication-quality plots, animations, colour scales, map projections, and
bitmap images. Several of these tools were used by Obreschkow et al.
(2020) <doi:10.1093/mnras/staa445>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
