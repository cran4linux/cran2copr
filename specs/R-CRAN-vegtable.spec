%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vegtable
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Handling Vegetation Data Sets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-taxlist >= 0.2.4
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegdata 
Requires:         R-CRAN-taxlist >= 0.2.4
Requires:         R-CRAN-foreign 
Requires:         R-methods 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-vegdata 

%description
Import and handling data from vegetation-plot databases, especially data
stored in 'Turboveg 2' (<https://www.synbiosys.alterra.nl/turboveg/>).
Also import/export routines for exchange of data with 'Juice'
(<https://www.sci.muni.cz/botany/juice/>) are implemented.

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
