%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kgen
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Calculating Stoichiometric Equilibrium Constants (Ks) for Seawater

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-pbapply >= 1.7.0
BuildRequires:    R-CRAN-reticulate >= 1.26
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-rappdirs >= 0.3.3
BuildRequires:    R-CRAN-rjson >= 0.2.21
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-pbapply >= 1.7.0
Requires:         R-CRAN-reticulate >= 1.26
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-rappdirs >= 0.3.3
Requires:         R-CRAN-rjson >= 0.2.21

%description
A unified software package simultaneously implemented in 'Python', 'R',
and 'Matlab' providing a uniform and internally-consistent way of
calculating stoichiometric equilibrium constants in modern and palaeo
seawater as a function of temperature, salinity, pressure and the
concentration of magnesium, calcium, sulphate, and fluorine.

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
