%global packname  ctrdata
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Retrieve and Analyze Clinical Trials in Public Registers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nodbi >= 0.3
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-nodbi >= 0.3
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 

%description
Provides functions for querying, retrieving and analysing protocol- and
results-related information on clinical trials from two public registers,
the European Union Clinical Trials Register (EUCTR,
<https://www.clinicaltrialsregister.eu/>) and ClinicalTrials.gov (CTGOV,
<https://clinicaltrials.gov/>). The information is transformed and then
stored in a database (nodbi). Functions are provided for accessing and
analysing the locally stored information on the clinical trials, as well
as for identifying duplicate records. The package is motivated by the need
for aggregating and trend-analysing the design, conduct and outcomes
across clinical trials.

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
%doc %{rlibdir}/%{packname}/exec
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/image
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
