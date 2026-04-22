%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Meanimiles
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Meanimiles

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fitdistrplus >= 1.2.6
BuildRequires:    R-CRAN-copula >= 1.1.7
BuildRequires:    R-stats 
Requires:         R-CRAN-fitdistrplus >= 1.2.6
Requires:         R-CRAN-copula >= 1.1.7
Requires:         R-stats 

%description
Provides a comprehensive suite of estimation tools for meanimiles, a
general class of (risk) functionals. This package includes nonparametric
estimators for univariate meanimile evaluation, copula-based estimation
for portfolio risk aggregation (full parametric, semiparametric, and
nonparametric), and novel estimators for meanimiles in regression
settings. Following the articles D. Debrauwer, I. Gijbels, and K. Herrmann
(2025) <doi:10.1214/25-EJS2391>, D. Debrauwer and I. Gijbels (2026)
<doi:10.1007/s00184-026-01022-9>.

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
