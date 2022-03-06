%global __brp_check_rpaths %{nil}
%global packname  quantilogram
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Quantilogram

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-stats 
Requires:         R-CRAN-np 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-SparseM 
Requires:         R-stats 

%description
Estimation and inference methods for the cross-quantilogram. The
cross-quantilogram is a measure of nonlinear dependence between two
variables, based on either unconditional or conditional quantile
functions.  The cross-quantilogram can be considered as an extension of
the correlogram, which is a correlation function over multiple lag periods
and mainly focuses on linear dependency.  One can use the
cross-quantilogram to detect the presence of directional predictability
from one time series to another.  This package provides a statistical
inference method based on the stationary bootstrap.  See Linton and Whang
(2007) <doi:10.1016/j.jeconom.2007.01.004> for univariate time series
analysis and Han, Linton, Oka and Whang (2016)
<doi:10.1016/j.jeconom.2016.03.001> for multivariate time series analysis.

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
