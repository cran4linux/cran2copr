%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  populR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Population Downscaling Using Areal Interpolation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-units 

%description
Downscaling of population data obtained by census surveys using areal
interpolation. Given a set of source zone polygons such as census tracts
or city blocks alongside with population counts and a target zone of
incogruent yet superimposed polygon features (such as individual
buildings) populR transforms population counts from the former to the
latter using Areal Weighting and Volume Weighting Interpolation methods.

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
