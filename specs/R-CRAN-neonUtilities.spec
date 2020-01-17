%global packname  neonUtilities
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          Utilities for Working with NEON Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gdata >= 2.18
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-gdata >= 2.18
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 

%description
NEON data packages can be accessed through the NEON Data Portal
<https://data.neonscience.org/home> or through the NEON Data API (see
<https://data.neonscience.org/data-api> for documentation). Data delivered
from the Data Portal are provided as monthly zip files packaged within a
parent zip file, while individual files can be accessed from the API. This
package provides tools that aid in discovering, downloading, and
reformatting data prior to use in analyses. This includes downloading data
via the API, merging data tables by type, and converting formats. For more
information, see the readme file at
<https://github.com/NEONScience/NEON-utilities>.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
