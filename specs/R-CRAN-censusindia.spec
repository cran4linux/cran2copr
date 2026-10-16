%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  censusindia
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Census of India Data, 1901-2011, with Boundaries and Projections

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
Tables from every decennial Census of India from 1901 to 2011: population
time series, Primary Census Abstracts at state, district and sub-district
level, mother tongue tables, and Scheduled Caste and Scheduled Tribe
populations, together with Ministry of Health and Family Welfare
population projections to 2036. Historical series are drawn from Jolad and
Singh (2026) <doi:10.7910/DVN/ON8CP8>. Census variables can be returned
with state or district boundaries of the matching census year attached for
mapping. Boundary files and the largest village-level tables are
downloaded on first use and cached locally.

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
