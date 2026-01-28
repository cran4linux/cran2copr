%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  campsismod
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generic Implementation of a PK/PD Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
A generic, easy-to-use and expandable implementation of a pharmacokinetic
(PK) / pharmacodynamic (PD) model based on the S4 class system. This
package allows the user to read and write pharmacometric models from and
to files, including a JSON-based interface to import Campsis models
defined using a formal JSON schema distributed with the package. Models
can be adapted further on the fly in the R environment using an intuitive
API to add, modify or delete equations, ordinary differential equations
(ODEs), model parameters or compartment properties (such as infusion
duration or rate, bioavailability and initial values). The package also
provides export facilities for use with the simulation packages ‘rxode2’
and ‘mrgsolve’. The package itself is licensed under the GPL (>= 3); the
JSON schema file shipped in inst/extdata is licensed separately under the
Creative Commons Attribution 4.0 International (CC BY 4.0).  This package
is designed and intended to be used with the package ‘campsis’, a PK/PD
simulation platform built on top of ‘rxode2’ and ‘mrgsolve’.

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
