%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  islandcodes
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reference Data and Helpers for Small Island States and Territories

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-countrycode >= 1.5.0
Requires:         R-CRAN-countrycode >= 1.5.0

%description
A curated reference list of countries and territories with classifications
for Small Island Developing States (SIDS), sub-national island
jurisdictions (SNIJ), World Bank region and income group, and political
association. Sub-sovereign cases such as Aruba, Curacao, Bonaire, Sint
Maarten, the French overseas territories, and Aaland Islands are
represented with disambiguating codes that standard country-code packages
often collapse or omit. Provides predicate helpers and a tidy joiner
intended to extend rather than replace 'countrycode'. Source data is
maintained at
<https://github.com/University-of-Aruba/island-research-reference-data>
and licensed CC BY 4.0.

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
