%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robustfa
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Object Oriented Solution for Robust Factor Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-stats 
Requires:         R-CRAN-rrcov 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-stats 

%description
Outliers virtually exist in any datasets of any application field. To
avoid the impact of outliers, we need to use robust estimators. Classical
estimators of multivariate mean and covariance matrix are the sample mean
and the sample covariance matrix. Outliers will affect the sample mean and
the sample covariance matrix, and thus they will affect the classical
factor analysis which depends on the classical estimators (Pison, G.,
Rousseeuw, P.J., Filzmoser, P. and Croux, C. (2003)
<doi:10.1016/S0047-259X(02)00007-6>). So it is necessary to use the robust
estimators of the sample mean and the sample covariance matrix. There are
several robust estimators in the literature: Minimum Covariance
Determinant estimator, Orthogonalized Gnanadesikan-Kettenring, Minimum
Volume Ellipsoid, M, S, and Stahel-Donoho. The most direct way to make
multivariate analysis more robust is to replace the sample mean and the
sample covariance matrix of the classical estimators to robust estimators
(Maronna, R.A., Martin, D. and Yohai, V. (2006) <doi:10.1002/0470010940>)
(Todorov, V. and Filzmoser, P. (2009) <doi:10.18637/jss.v032.i03>), which
is our choice of robust factor analysis. We created an object oriented
solution for robust factor analysis based on new S4 classes.

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
