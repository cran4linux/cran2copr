%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ffstream
%global packver   0.1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Forgetting Factor Methods for Change Detection in Streaming Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 

%description
An implementation of the adaptive forgetting factor scheme described in
Bodenham and Adams (2016) <doi:10.1007/s11222-016-9684-8> which adaptively
estimates the mean and variance of a stream in order to detect multiple
changepoints in streaming data. The implementation is in 'C++' and uses
'Rcpp'. Additionally, implementations of the fixed forgetting factor
scheme from the same paper, as well as the classic cumulative sum
('CUSUM') and exponentially weighted moving average ('EWMA') methods, are
included.

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
