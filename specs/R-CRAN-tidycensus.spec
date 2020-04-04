%global packname  tidycensus
%global packver   0.9.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9.2
Release:          1%{?dist}
Summary:          Load US Census Boundary and Attribute Data as 'tidyverse' and'sf'-Ready Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.7.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tigris 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.5.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.7.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tigris 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
An integrated R interface to the decennial US Census and American
Community Survey APIs and the US Census Bureau's geographic boundary
files.  Allows R users to return Census and ACS data as tidyverse-ready
data frames, and optionally returns a list-column with feature geometry
for many geographies.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
