%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimuRg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Building, Fitting and Evaluating PK/PD Modeles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-philentropy 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-synthpop 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-philentropy 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rxode2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-synthpop 
Requires:         R-CRAN-sys 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-withr 

%description
Provides a unified workflow for building, fitting using external engines,
and evaluating ordinary differential equation (ODE)-based
pharmacokinetic/pharmacodynamic (PK/PD) models. Supports generation of
estimation scenarios and control files for external engines (e.g.,
'Monolix'), simulation of models using 'rxode2', and creation of
goodness-of-fit diagnostics. Includes tools for covariate modeling,
virtual population design, and local and global sensitivity analyses.

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
