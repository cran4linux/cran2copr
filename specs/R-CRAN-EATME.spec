%global __brp_check_rpaths %{nil}
%global packname  EATME
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exponentially Weighted Moving Average with Adjustments to Measurement Error

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-qcr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-qcr 
Requires:         R-stats 
Requires:         R-graphics 

%description
The univariate statistical quality control tool aims to address
measurement error effects when constructing exponentially weighted moving
average p control charts. The method primarily focuses on binary random
variables, but it can be applied to any continuous random variables by
using sign statistic to transform them to discrete ones. With the
correction of measurement error effects, we can obtain the corrected
control limits of exponentially weighted moving average p control chart
and reasonably adjusted exponentially weighted moving average p control
charts. The methods in this package can be found in some relevant
references, such as Chen and Yang (2022) <arXiv: 2203.03384>; Yang et al.
(2011) <doi: 10.1016/j.eswa.2010.11.044>; Yang and Arnold (2014) <doi:
10.1155/2014/238719>; Yang (2016) <doi: 10.1080/03610918.2013.763980> and
Yang and Arnold (2016) <doi: 10.1080/00949655.2015.1125901>.

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
