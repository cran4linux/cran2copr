%global __brp_check_rpaths %{nil}
%global packname  Rilostat
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          ILO Open Data via Ilostat Bulk Download Facility or SDMX Web Service

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-tibble >= 3.0.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-DT 

%description
Tools to download data from the ilostat database <https://ilostat.ilo.org>
together with search and manipulation utilities.

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
