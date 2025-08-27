%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sae2
%global packver   1.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Estimation: Time-Series Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-survey 
Requires:         R-stats 

%description
Time series area-level models for small area estimation. The package
supplements the functionality of the sae package. Specifically, it
includes EBLUP fitting of the Rao-Yu model in the original form without a
spatial component. The package also offers a modified ("dynamic") version
of the Rao-Yu model, replacing the assumption of stationarity. Both
univariate and multivariate applications are supported. Of particular note
is the allowance for covariance of the area-level sample estimates over
time, as encountered in rotating panel designs such as the U.S. National
Crime Victimization Survey or present in a time-series of 5-year estimates
from the American Community Survey. Key references to the methods include
J.N.K. Rao and I. Molina (2015, ISBN:9781118735787), J.N.K. Rao and M. Yu
(1994) <doi:10.2307/3315407>, and R.E. Fay and R.A. Herriot (1979)
<doi:10.1080/01621459.1979.10482505>.

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
