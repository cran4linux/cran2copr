%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weightedRank
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis Using Weighted Rank Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sensitivitymv 
BuildRequires:    R-CRAN-senstrat 
BuildRequires:    R-CRAN-BiasedUrn 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sensitivitymv 
Requires:         R-CRAN-senstrat 
Requires:         R-CRAN-BiasedUrn 

%description
Performs a sensitivity analysis using weighted rank tests in observational
studies with I blocks of size J; see Rosenbaum (2024)
<doi:10.1080/01621459.2023.2221402>.  The package can perform adaptive
inference in block designs; see Rosenbaum (2012)
<doi:10.1093/biomet/ass032>.  The package can increase design sensitivity
using the conditioning tactic in Rosenbaum (2025)
<doi:10.1093/jrsssb/qkaf007>.  The main functions are wgtRank(),
wgtRankCI(), wgtRanktt() and wgtRankC().

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
