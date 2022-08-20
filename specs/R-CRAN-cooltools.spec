%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cooltools
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Practical Tools for Scientific Computations and Visualizations

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
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-celestial 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pracma 
Requires:         R-utils 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-Rcpp 

%description
Collection of routines for efficient scientific computations in physics
and astrophysics. These routines include utility functions, numerical
computation tools, as well as visualisation tools. They can be used, for
example, for generating random numbers from spherical and custom
distributions, information and entropy analysis, special Fourier
transforms, two-point correlation estimation (e.g. as in Landy & Szalay
(1993) <doi:10.1086/172900>), binning & gridding of point sets, 2D
interpolation, Monte Carlo integration, vector arithmetic and coordinate
transformations. Also included is a non-exhaustive list of important
constants and cosmological conversion functions. The graphics routines can
be used to produce and export publication-ready scientific plots and
movies, e.g. as used in Obreschkow et al. (2020)
<doi:10.1093/mnras/staa445>. These routines include special color scales,
projection functions, and bitmap handling routines.

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
