%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GaussSuppression
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tabular Data Suppression using Gaussian Elimination

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SSBtools >= 1.4.3
BuildRequires:    R-CRAN-RegSDC >= 0.7.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-SSBtools >= 1.4.3
Requires:         R-CRAN-RegSDC >= 0.7.0
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-methods 

%description
A statistical disclosure control tool to protect tables by suppression
using the Gaussian elimination secondary suppression algorithm. A
suggestion is to start by working with functions SuppressSmallCounts() and
SuppressDominantCells(). These functions use primary suppression functions
for the minimum frequency rule and the dominance rule, respectively. Novel
functionality for suppression of disclosive cells is also included.
General primary suppression functions can be supplied as input to the
general working horse function, GaussSuppressionFromData(). Suppressed
frequencies can be replaced by synthetic decimal numbers as described in
Langsrud (2019) <doi:10.1007/s11222-018-9848-9>.

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
