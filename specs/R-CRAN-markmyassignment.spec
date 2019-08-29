%global packname  markmyassignment
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          Automatic Marking of R Assignments

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 2.0.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-checkmate >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-testthat >= 2.0.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-checkmate >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-yaml 
Requires:         R-codetools 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-rlang 

%description
Automatic marking of R assignments for students and teachers based on
'testthat' test suites.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
