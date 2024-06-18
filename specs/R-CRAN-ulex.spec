%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ulex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unique Location Extractor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-ngram 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-spacyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-ngram 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-raster 
Requires:         R-parallel 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-spacyr 
Requires:         R-utils 

%description
Extracts coordinates of an event location from text based on dictionaries
of landmarks, roads, and areas. Only returns the location of an event of
interest and ignores other location references; for example, if
determining the location of a road traffic crash from the text "crash near
[location 1] heading towards [location 2]", only the coordinates of
"location 1" would be returned. Moreover, accounts for differences in
spelling between how a user references a location and how a location is
captured in location dictionaries.

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
