%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tweedie
%global packver   3.0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.14
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation of Tweedie Exponential Family Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildRequires:    R-CRAN-statmod >= 1.4.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-statmod >= 1.4.0
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 

%description
Maximum likelihood computations for Tweedie families, including the series
expansion (Dunn and Smyth, 2005; <doi:10.1007/s11222-005-4070-y>) and the
Fourier inversion (Dunn and Smyth, 2008; <doi:10.1007/s11222-007-9039-6>),
and related methods.

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
