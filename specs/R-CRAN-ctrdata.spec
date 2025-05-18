%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctrdata
%global packver   1.22.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.22.2
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve and Analyze Clinical Trials Data from Public Registers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.1.0
BuildRequires:    R-CRAN-nodbi >= 0.10.7
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-jqr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-curl >= 5.1.0
Requires:         R-CRAN-nodbi >= 0.10.7
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-jqr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tidyr 

%description
A system for querying, retrieving and analyzing protocol- and
results-related information on clinical trials from four public registers,
the 'European Union Clinical Trials Register' ('EUCTR',
<https://www.clinicaltrialsregister.eu/>), 'ClinicalTrials.gov'
(<https://clinicaltrials.gov/> and also translating queries the retired
classic interface), the 'ISRCTN' (<http://www.isrctn.com/>) and the
'European Union Clinical Trials Information System' ('CTIS',
<https://euclinicaltrials.eu/>). Trial information is downloaded,
converted and stored in a database ('PostgreSQL', 'SQLite', 'DuckDB' or
'MongoDB'; via package 'nodbi'). Protocols, statistical analysis plans,
informed consent sheets and other documents in registers associated with
trials can also be downloaded. Other functions implement trial concepts
canonically across registers, identify deduplicated records, easily find
and extract variables (fields) of interest even from complex nested data
as used by the registers, merge variables and update queries. The package
can be used for monitoring, meta- and trend-analysis of the design and
conduct as well as of the results of clinical trials across registers.

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
