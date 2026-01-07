%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbrsa
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fetch Turkish Banking Sector Data from the Turkish Banking Regulation and Supervision Agency

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-writexl 

%description
The goal of the 'rbrsa' package is to provide automated access to banking
sector data from the Turkish Banking Regulation and Supervision Agency
(BRSA, known as BDDK in Turkish). The package retrieves tables from two
distinct publication portals maintained by the BRSA: The Monthly Bulletin
Portal <https://www.bddk.org.tr/bultenaylik> and The FinTurk Data System
<https://www.bddk.org.tr/BultenFinturk>.

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
