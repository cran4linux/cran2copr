%global __brp_check_rpaths %{nil}
%global packname  SLBDD
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Learning for Big Dependent Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-gsarima 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MTS 
BuildRequires:    R-CRAN-TSclust 
BuildRequires:    R-CRAN-tsoutliers 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-rnn 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-gsarima 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-imputeTS 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MTS 
Requires:         R-CRAN-TSclust 
Requires:         R-CRAN-tsoutliers 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-rnn 

%description
Programs for analyzing large-scale time series data. They include
functions for automatic specification and estimation of univariate time
series, for clustering time series, for multivariate outlier detections,
for quantile plotting of many time series, for dynamic factor models and
for creating input data for deep learning programs. Examples of using the
package can be found in the Wiley book 'Statistical Learning with Big
Dependent Data' by Daniel Peña and Ruey S. Tsay (2021). ISBN
9781119417385.

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
