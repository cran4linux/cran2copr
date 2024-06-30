%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gms
%global packver   0.31.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.31.2
Release:          1%{?dist}%{?buildtag}
Summary:          'GAMS' Modularization Support Package

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-filelock 
Requires:         R-stats 

%description
A collection of tools to create, use and maintain modularized model code
written in the modeling language 'GAMS' (<https://www.gams.com/>).
Out-of-the-box 'GAMS' does not come with support for modularized model
code. This package provides the tools necessary to convert a standard
'GAMS' model to a modularized one by introducing a modularized code
structure together with a naming convention which emulates local
environments. In addition, this package provides tools to monitor the
compliance of the model code with modular coding guidelines.

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
