%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastbioclim
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable and Flexible Derivation of Custom-Time Bioclimatic and Environmental Summary Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.0
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-terra >= 1.7.0
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-sf 

%description
Provides an efficient tool for creating custom-time bioclimatic and
derived environmental summary variables from user-supplied raster data for
user-defined timeframes. The package overcomes computational bottlenecks
by automatically switching between an in-memory framework using the
'terra' package to maximize speed for smaller datasets, and an on-disk
tiling framework for rasters that exceed available RAM, leveraging
'exactextractr' and 'Rfast' to process data in chunks. The core functions,
derive_bioclim() and derive_statistics(), offer a unified interface with
flexibility for custom time periods beyond standard quarters and the use
of fixed temporal indices, facilitating the creation of temporally-matched
environmental variables for ecological and biogeographical modeling. Visit
the package website <https://gepinillab.github.io/fastbioclim/> to find
tutorials in English and Spanish.

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
