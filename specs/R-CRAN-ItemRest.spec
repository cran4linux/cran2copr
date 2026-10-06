%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ItemRest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Item Removal Strategies for Exploratory Factor Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-qgraph 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Identifies candidate item sets through threshold-driven iterative removal
searches in exploratory factor analysis. Provides a no-removal baseline,
numerical diagnostics, factor reliability, holdout evaluation, and
bootstrap search stability to support transparent screening and documented
content review rather than automatic measurement decisions. The loading
criteria are based on best practices and established heuristics (e.g.,
Costello & Osborne (2005) <doi:10.7275/jyj1-4868>, Howard (2016)
<doi:10.1080/10447318.2015.1087664>). Includes flexible thresholds for
factor loadings (min_loading) and cross-loading differences
(loading_diff).

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
