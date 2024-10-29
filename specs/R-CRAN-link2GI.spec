%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  link2GI
%global packver   0.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Linking Geographic Information Systems, Remote Sensing and Other Command Line Tools

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.9
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-renv 
Requires:         R-CRAN-sf >= 0.9
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-terra 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-renv 

%description
Functions and tools for using open GIS and remote sensing command-line
interfaces in a reproducible environment.

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
