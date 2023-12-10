%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frechet
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis for Random Objects and Non-Euclidean Data

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fdapace >= 0.5.5
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-fdadensity 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-utils 
Requires:         R-CRAN-fdapace >= 0.5.5
Requires:         R-CRAN-boot 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-fdadensity 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-osqp 
Requires:         R-stats 
Requires:         R-CRAN-trust 
Requires:         R-utils 

%description
Provides implementation of statistical methods for random objects lying in
various metric spaces, which are not necessarily linear spaces. The core
of this package is Fréchet regression for random objects with Euclidean
predictors, which allows one to perform regression analysis for
non-Euclidean responses under some mild conditions. Examples include
distributions in 2-Wasserstein space, covariance matrices endowed with
power metric (with Frobenius metric as a special case), Cholesky and
log-Cholesky metrics, spherical data. References: Petersen, A., & Müller,
H.-G. (2019) <doi:10.1214/17-AOS1624>.

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
