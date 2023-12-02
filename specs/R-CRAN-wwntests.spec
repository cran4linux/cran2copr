%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wwntests
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Tests for Functional Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ftsa 
BuildRequires:    R-CRAN-rainbow 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-fda 
Requires:         R-CRAN-sde 
Requires:         R-stats 
Requires:         R-CRAN-ftsa 
Requires:         R-CRAN-rainbow 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-CRAN-fda 

%description
Provides a collection of white noise hypothesis tests for functional time
series and related visualizations. These include tests based on the norms
of autocovariance operators that are built under both strong and weak
white noise assumptions. Additionally, tests based on the spectral density
operator and on principal component dimensional reduction are included,
which are built under strong white noise assumptions. Also, this package
provides goodness-of-fit tests for functional autoregressive of order 1
models. These methods are described in Kokoszka et al. (2017)
<doi:10.1016/j.jmva.2017.08.004>, Characiejus and Rice (2019)
<doi:10.1016/j.ecosta.2019.01.003>, Gabrys and Kokoszka (2007)
<doi:10.1198/016214507000001111>, and Kim et al. (2023) <doi:
10.1214/23-SS143> respectively.

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
