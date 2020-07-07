%global packname  heims
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Decode and Validate HEIMS Data from Department of Education,Australia

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hutils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hutils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-lubridate 

%description
Decode elements of the Australian Higher Education Information Management
System (HEIMS) data for clarity and performance. HEIMS is the record
system of the Department of Education, Australia to record enrolments and
completions in Australia's higher education system, as well as a range of
relevant information. For more information, including the source of the
data dictionary, see
<http://heimshelp.education.gov.au/sites/heimshelp/dictionary/pages/data-element-dictionary>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
