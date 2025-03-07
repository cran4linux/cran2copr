%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fkbma
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Free Knot-Bayesian Model Averaging

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-matrixStats 
Requires:         R-splines 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstantools

%description
Analysis of Bayesian adaptive enrichment clinical trial using Free-Knot
Bayesian Model Averaging (FK-BMA) method of Maleyeff et al. (2024) for
Gaussian data. Maleyeff, L., Golchi, S., Moodie, E. E. M., & Hudson, M.
(2024) "An adaptive enrichment design using Bayesian model averaging for
selection and threshold-identification of predictive variables"
<doi:10.1093/biomtc/ujae141>.

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
