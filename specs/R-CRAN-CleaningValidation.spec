%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CleaningValidation
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cleaning Validation Functions for Pharmaceutical Cleaning Process

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dunn.test 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dunn.test 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-lme4 

%description
Provides essential Cleaning Validation functions for complying with
pharmaceutical cleaning process regulatory standards. The package includes
non-parametric methods to analyze drug active-ingredient residue (DAR),
cleaning agent residue (CAR), and microbial colonies (Mic) for non-Poisson
distributions. Additionally, Poisson methods are provided for Mic analysis
when Mic data follow a Poisson distribution.

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
