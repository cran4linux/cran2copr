%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesnec
%global packver   2.1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Bayesian No-Effect- Concentration (NEC) Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-chk >= 0.7.0
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-chk >= 0.7.0
Requires:         R-CRAN-brms 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-rlang 

%description
Implementation of No-Effect-Concentration estimation that uses 'brms' (see
Burkner (2017)<doi:10.18637/jss.v080.i01>; Burkner
(2018)<doi:10.32614/RJ-2018-017>; Carpenter 'et al.'
(2017)<doi:10.18637/jss.v076.i01> to fit concentration(dose)-response data
using Bayesian methods for the purpose of estimating 'ECX' values, but
more particularly 'NEC' (see Fox (2010)<doi:10.1016/j.ecoenv.2009.09.012>.
This package expands and supersedes an original version implemented in
R2jags, see Fisher, Ricardo and Fox (2020)<doi:10.5281/ZENODO.3966864>.

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
