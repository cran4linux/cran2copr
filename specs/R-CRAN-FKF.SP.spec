%global packname  FKF.SP
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Kalman Filtering Through Sequential Processing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-curl 

%description
Fast and flexible Kalman filtering implementation utilizing sequential
processing, designed for efficient parameter estimation through maximum
likelihood estimation. Sequential processing is a univariate treatment of
a multivariate series of observations and can benefit from computational
efficiency over traditional Kalman filtering when independence is assumed
in the variance of the disturbances of the measurement equation.
Sequential processing is described in the textbook of Durbin and Koopman
(2001, ISBN:978-0-19-964117-8). 'FKF.SP' was built upon the existing 'FKF'
package and is, in general, a faster Kalman filter.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
