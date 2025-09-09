%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  COINT
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unit Root Tests with Structural Breaks and Fully-Modified Estimators

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-timeSeries 
Requires:         R-CRAN-timeSeries 

%description
Procedures include Phillips (1995) FMVAR <doi:10.2307/2171721>, Kitamura
and Phillips (1997) FMGMM <doi:10.1016/S0304-4076(97)00004-3>, and Park
(1992) CCR <doi:10.2307/2951679>, and so on. Tests with 1 or 2 structural
breaks include Gregory and Hansen (1996)
<doi:10.1016/0304-4076(69)41685-7>, Zivot and Andrews (1992)
<doi:10.2307/1391541>, and Kurozumi (2002)
<doi:10.1016/S0304-4076(01)00106-3>.

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
