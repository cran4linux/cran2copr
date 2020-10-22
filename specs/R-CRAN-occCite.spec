%global packname  occCite
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Querying and Managing Large Biodiversity Occurrence Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgbif >= 3.1
BuildRequires:    R-CRAN-bib2df 
BuildRequires:    R-CRAN-BIEN 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-waffle 
Requires:         R-CRAN-rgbif >= 3.1
Requires:         R-CRAN-bib2df 
Requires:         R-CRAN-BIEN 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-knitr 
Requires:         R-stats 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-waffle 

%description
Facilitates the gathering of biodiversity occurrence data from disparate
sources. Metadata is managed throughout the process to facilitate
reporting and enhanced ability to repeat analyses.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
