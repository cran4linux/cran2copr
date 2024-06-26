%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsocialwatcher
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Facebook Marketing API' Social Watcher

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-splitstackshape 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-purrr 

%description
Facilitates querying data from the ‘Facebook Marketing API', particularly
for social science research
<https://developers.facebook.com/docs/marketing-apis/>. Data from the
'Facebook Marketing API' has been used for a variety of social science
applications, such as for poverty estimation (Marty and Duhaut (2024)
<doi:10.1038/s41598-023-49564-6>), disease surveillance (Araujo et al.
(2017) <doi:10.48550/arXiv.1705.04045>), and measuring migration
(Alexander, Polimis, and Zagheni (2020) <doi:10.1007/s11113-020-09599-3>).
The package facilitates querying the number of Facebook daily/monthly
active users for multiple location types (e.g., from around a specific
coordinate to an administrative region) and for a number of attribute
types (e.g., interests, behaviors, education level, etc). The package
supports making complex queries within one API call and making multiple
API calls across different locations and/or parameters.

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
