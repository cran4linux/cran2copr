%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  perufaunads004
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Taxonomic Validation and Reconciliation of Threatened Fauna of Peru

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-stringdist >= 0.9.8
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-stringdist >= 0.9.8
Requires:         R-CRAN-cli 

%description
Taxonomic validation and reconciliation of scientific names of threatened
and legally protected wildlife species in Peru, based on Supreme Decree
No. 004-2014-MINAGRI (MINAGRI, 2014)
<https://www.midagri.gob.pe/portal/decreto-supremo/ds-2014/10837-decreto-supremo-n-004-2014-minagri>
and the "Libro Rojo de la Fauna Silvestre Amenazada del Peru" (SERFOR,
2018, ISBN:978-612-46908-2-2). Provides taxonomic name parsing, a
hierarchical matching engine (exact, synonym, fuzzy, and genus-level), and
structured access to conservation technical sheets.

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
