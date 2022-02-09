%global __brp_check_rpaths %{nil}
%global packname  physx
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Scientific Computations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-celestial 
BuildRequires:    R-CRAN-docore 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-celestial 
Requires:         R-CRAN-docore 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pracma 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-Rcpp 

%description
Collection of auxiliary routines for efficient scientific computations in
physics and astrophysics. These routines can be used for random number
generation (e.g. from spherical and custom distributions), information and
entropy analysis (e.g. used in Obreschkow et al. (2020)
<doi:10.1093/mnras/staa445>), spatial statistics, such as special DFTs and
Landy-Szalay estimators (Landy & Szalay (1993) <doi:10.1086/172900>),
binning/gridding of point sets and 2D interpolation, Monte Carlo
integration, vector arithmetics, coordinate transformations, unit
conversions and cosmological distance calculations. Also includes a list
of important physical constants, particularly useful in astrophysics.

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
