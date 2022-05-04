%global __brp_check_rpaths %{nil}
%global packname  robcp
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Change-Point Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Provides robust methods to detect change-points in uni- or multivariate
time series. They can cope with corrupted data and heavy tails. Focus is
on the detection of abrupt changes in location, but changes scale or
dependence structure can be detected as well. This package provides tests
for change detection in uni- and multivariate time series based on
Huberized versions of CUSUM tests proposed in Duerre and Fried (2019)
<arXiv:1905.06201>, and tests for change detection in univariate time
series based on 2-sample U-statistics or 2-sample U-quantiles as proposed
by Dehling et al. (2015) <DOI:10.1007/978-1-4939-3076-0_12> and Dehling,
Fried and Wendler (2020) <DOI:10.1093/biomet/asaa004>. Furthermore, the
packages provides tests on changes in the scale or the correlation as
proposed in Gerstenberger, Vogel and Wendler (2020)
<DOI:10.1080/01621459.2019.1629938>, Dehling et al. (2017)
<DOI:10.1017/S026646661600044X>, and Wied et al. (2014)
<DOI:10.1016/j.csda.2013.03.005>.

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
