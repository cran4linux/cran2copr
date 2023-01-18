%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ads
%global packver   1.5-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.9
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Point Patterns Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-spatstat.geom 

%description
Perform first- and second-order multi-scale analyses derived from Ripley
K-function (Ripley B. D. (1977) <doi:10.1111/j.2517-6161.1977.tb01615.x>),
for univariate, multivariate and marked mapped data in rectangular,
circular or irregular shaped sampling windows, with tests of statistical
significance based on Monte Carlo simulations.

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
