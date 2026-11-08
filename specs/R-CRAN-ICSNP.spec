%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICSNP
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Multivariate Nonparametrics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ICS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ICS 

%description
Classical multivariate methods such as Hotelling's T-test are based on the
sample mean vector and the sample covariance matrix, which makes them
sensitive to outliers and heavy-tailed distributions. The package provides
nonparametric alternatives based on marginal ranks, spatial signs and
spatial ranks, as reviewed for example in Nordhausen and Oja (2018)
<doi:10.1146/annurev-statistics-031017-100247>. It contains tests for
location and independence, Hotelling's T-test as a parametric reference,
the spatial median and other location estimates, and several estimates of
shape. The tests can also be applied to invariant coordinates obtained
with the package 'ICS'.

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
