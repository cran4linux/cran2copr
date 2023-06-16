%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reslr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Relative Sea Level Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidybayes 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidybayes 
Requires:         R-CRAN-tidyr 

%description
The Bayesian modelling of relative sea-level data using a comprehensive
approach that incorporates various statistical models within a unifying
framework. Details regarding each statistical models; linear regression
(Ashe et al 2019) <doi:10.1016/j.quascirev.2018.10.032>, change point
models (Cahill et al 2015) <doi:10.1088/1748-9326/10/8/084002>, integrated
Gaussian process models (Cahill et al 2015) <doi:10.1214/15-AOAS824>,
temporal splines (Upton et al 2023) <arXiv:2301.09556>, spatio-temporal
splines (Upton et al 2023) <arXiv:2301.09556> and generalised additive
models (Upton et al 2023) <arXiv:2301.09556>. This package facilitates
data loading, model fitting and result summarisation. Notably, it
accommodates the inherent measurement errors found in relative sea-level
data across multiple dimensions, allowing for their inclusion in the
statistical models.

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
