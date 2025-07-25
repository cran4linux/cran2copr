%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  testcorr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Testing Zero Correlation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Computes the test statistics for examining the significance of
autocorrelation in univariate time series, cross-correlation in bivariate
time series, Pearson correlations in multivariate series and test
statistics for i.i.d. property of univariate series given in Dalla,
Giraitis and Phillips (2022),
<https://www.cambridge.org/core/journals/econometric-theory/article/abs/robust-tests-for-white-noise-and-crosscorrelation/4D77C12C52433F4C6735E584C779403A>,
<https://elischolar.library.yale.edu/cowles-discussion-paper-series/57/>.

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
