%global __brp_check_rpaths %{nil}
%global packname  PDMIF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fits Heterogeneous Panel Data Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-diagonals 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-diagonals 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-quantreg 

%description
Fits heterogeneous panel data models with interactive effects for linear
regression, logistic, count, probit, quantile, and clustering. Based on
Ando, T. and Bai, J. (2015) "A simple new test for slope homogeneity in
panel data models with interactive effects" <doi:
10.1016/j.econlet.2015.09.019>, Ando, T. and Bai, J. (2015) "Asset Pricing
with a General Multifactor Structure" <doi: 10.1093/jjfinex/nbu026> ,
Ando, T. and Bai, J. (2016) "Panel data models with grouped factor
structure under unknown group membership" <doi: 10.1002/jae.2467>, Ando,
T. and Bai, J. (2017) "Clustering huge number of financial time series: A
panel data approach with high-dimensional predictors and factor
structures" <doi: 10.1080/01621459.2016.1195743>, Ando, T. and Bai, J.
(2020) "Quantile co-movement in financial markets" <doi:
10.1080/01621459.2018.1543598>, Ando, T., Bai, J. and Li, K. (2021)
"Bayesian and maximum likelihood analysis of large-scale panel choice
models with unobserved heterogeneity" <doi:
10.1016/j.jeconom.2020.11.013.>.

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
