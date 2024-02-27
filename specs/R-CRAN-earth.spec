%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  earth
%global packver   5.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Adaptive Regression Splines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-plotmo >= 3.6.0
BuildRequires:    R-CRAN-Formula >= 1.2.3
Requires:         R-CRAN-plotmo >= 3.6.0
Requires:         R-CRAN-Formula >= 1.2.3

%description
Build regression models using the techniques in Friedman's papers "Fast
MARS" and "Multivariate Adaptive Regression Splines"
<doi:10.1214/aos/1176347963>. (The term "MARS" is trademarked and thus not
used in the name of the package.)

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
