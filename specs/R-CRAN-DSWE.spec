%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DSWE
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Data Science for Wind Energy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-KernSmooth >= 2.23.16
BuildRequires:    R-CRAN-gss >= 2.2.2
BuildRequires:    R-CRAN-e1071 >= 1.7.3
BuildRequires:    R-CRAN-FNN >= 1.1.3
BuildRequires:    R-CRAN-mixtools >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.870.2.0
BuildRequires:    R-CRAN-matrixStats >= 0.55.0
BuildRequires:    R-CRAN-BayesTree >= 0.3.1.4
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-KernSmooth >= 2.23.16
Requires:         R-CRAN-gss >= 2.2.2
Requires:         R-CRAN-e1071 >= 1.7.3
Requires:         R-CRAN-FNN >= 1.1.3
Requires:         R-CRAN-mixtools >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-matrixStats >= 0.55.0
Requires:         R-CRAN-BayesTree >= 0.3.1.4

%description
Data science methods used in wind energy applications. Current
functionalities include creating a multi-dimensional power curve model,
performing power curve function comparison, covariate matching, and energy
decomposition. Relevant works for the developed functions are: funGP() -
Prakash et al. (2022) <doi:10.1080/00401706.2021.1905073>, AMK() - Lee et
al. (2015) <doi:10.1080/01621459.2014.977385>, tempGP() - Prakash et al.
(2022) <doi:10.1080/00401706.2022.2069158>, ComparePCurve() - Ding et al.
(2021) <doi:10.1016/j.renene.2021.02.136>, deltaEnergy() - Latiffianti et
al. (2022) <doi:10.1002/we.2722>, syncSize() - Latiffianti et al. (2022)
<doi:10.1002/we.2722>, imptPower() - Latiffianti et al. (2022)
<doi:10.1002/we.2722>, All other functions - Ding (2019,
ISBN:9780429956508).

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
