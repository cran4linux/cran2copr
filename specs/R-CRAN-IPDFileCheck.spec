%global packname  IPDFileCheck
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          2%{?dist}
Summary:          Basic Functions to Check Readability, Consistency, and Contentof an Individual Participant Data File

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 1.0.2
BuildRequires:    R-CRAN-GlobalOptions >= 0.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-eeptools 
Requires:         R-CRAN-testthat >= 1.0.2
Requires:         R-CRAN-GlobalOptions >= 0.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-eeptools 

%description
Basic checks needed with an individual level participant data from
randomised controlled trial. This checks files for existence, read access
and individual columns for formats. The checks on format is currently
implemented for gender and age formats.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
