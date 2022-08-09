%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  standartox
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Ecotoxicological Information from the Standartox Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-fst >= 0.9.4
BuildRequires:    R-stats 
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-fst >= 0.9.4
Requires:         R-stats 

%description
The <http://standartox.uni-landau.de> database offers cleaned, harmonized
and aggregated ecotoxicological test data, which can be used for assessing
effects and risks of chemical concentrations found in the environment.

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
