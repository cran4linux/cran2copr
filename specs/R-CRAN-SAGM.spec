%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SAGM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Autoregressive Graphical Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.10
Requires:         R-core >= 3.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fastmatrix 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-fastmatrix 
Requires:         R-CRAN-GIGrvg 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 

%description
Implements the methodological developments found in Hermes, van
Heerwaarden, and Behrouzi (2023) <doi:10.48550/arXiv.2308.04325>, and
allows for the statistical modeling of asymmetric between-location
effects, as well as within-location effects using spatial autoregressive
graphical models. The package allows for the generation of spatial weight
matrices to capture asymmetric effects for strip-type intercropping
designs, although it can handle any type of spatial data commonly found in
other sciences.

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
