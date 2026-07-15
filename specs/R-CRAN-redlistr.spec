%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  redlistr
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the IUCN Red List of Ecosystems and Species

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.8.54
BuildRequires:    R-CRAN-sf >= 1.0.21
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-terra >= 1.8.54
Requires:         R-CRAN-sf >= 1.0.21
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-units 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-mgcv 

%description
A toolbox created by members of the International Union for Conservation
of Nature (IUCN) Red List of Ecosystems Committee for Scientific
Standards. Primarily, it is a set of tools suitable for calculating the
metrics required for making assessments of species and ecosystems against
the IUCN Red List of Threatened Species and the IUCN Red List of
Ecosystems categories and criteria. See the IUCN website for detailed
guidelines, the criteria, publications and other information.

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
