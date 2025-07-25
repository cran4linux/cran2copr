%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  L1pack
%global packver   0.60
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.60
Release:          1%{?dist}%{?buildtag}
Summary:          Routines for L1 Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-fastmatrix 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-fastmatrix 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
L1 estimation for linear regression using Barrodale and Roberts' method
<doi:10.1145/355616.361024> and the EM algorithm
<doi:10.1023/A:1020759012226>. Estimation of mean and covariance matrix
using the multivariate Laplace distribution, density, distribution
function, quantile function and random number generation for univariate
and multivariate Laplace distribution <doi:10.1080/03610929808832115>.
Implementation of Naik and Plungpongpun <doi:10.1007/0-8176-4487-3_7> for
the Generalized spatial median estimator is included.

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
