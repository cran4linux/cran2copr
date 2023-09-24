%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcompanion
%global packver   0.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Objects and Methods for Multi-Companion Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gbutils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-methods 
Requires:         R-CRAN-gbutils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rdpack 

%description
Provides a class for multi-companion matrices with methods for arithmetic
and factorization.  A method for generation of multi-companion matrices
with prespecified spectral properties is provided, as well as some
utilities for periodically correlated and multivariate time series models.
See Boshnakov (2002) <doi:10.1016/S0024-3795(01)00475-X> and Boshnakov &
Iqelan (2009) <doi:10.1111/j.1467-9892.2009.00617.x>.

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
