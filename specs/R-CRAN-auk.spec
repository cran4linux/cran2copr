%global packname  auk
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          eBird Data Extraction and Processing in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-countrycode >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-countrycode >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Extract and process bird sightings records from eBird
(<http://ebird.org>), an online tool for recording bird observations.
Public access to the full eBird database is via the eBird Basic Dataset
(EBD; see <http://ebird.org/ebird/data/download> for access), a
downloadable text file. This package is an interface to AWK for extracting
data from the EBD based on taxonomic, spatial, or temporal filters, to
produce a manageable file size that can be imported into R.

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
