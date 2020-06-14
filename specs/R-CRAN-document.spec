%global packname  document
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          2%{?dist}
Summary:          Run 'roxygen2' on (Chunks of) Single Code Files

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-rcmdcheck 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-rcmdcheck 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-withr 

%description
Have you ever been tempted to create 'roxygen2'-style documentation
comments for one of your functions that was not part of one of your
packages (yet)? This is exactly what this package is about: running
'roxygen2' on (chunks of) a single code file.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/expected_files
%doc %{rlibdir}/%{packname}/files
%doc %{rlibdir}/%{packname}/runit_tests
%{rlibdir}/%{packname}/INDEX
