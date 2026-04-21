%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gerda
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          German Election Database (GERDA)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tibble 

%description
Provides tools to download datasets of German elections covering local,
state, federal, mayoral, European Parliament, and county (Kreistag)
elections, with federal county-level coverage from 1953 and other families
extending through 2025. The package supplies turnout, vote shares, and
derived indicators at the municipal and county level, including
geographically harmonized datasets that account for changes in municipal
boundaries over time and incorporate mail-in voting districts. Bundled
data includes county-level INKAR covariates (1995-2022) and
municipality-level Zensus 2022 indicators. Data is sourced from
<https://github.com/awiedem/german_election_data>.

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
