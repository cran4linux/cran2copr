%global packname  openxlsx
%global packver   4.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.0.1
Release:          1%{?dist}
Summary:          Read, Write and Edit XLSX Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zip 

%description
Simplifies the creation of Excel .xlsx files by providing a high level
interface to writing, styling and editing worksheets. Through the use of
'Rcpp', read/write times are comparable to the 'xlsx' and 'XLConnect'
packages with the added benefit of removing the dependency on Java.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/build_font_size_lookup.R
%doc %{rlibdir}/%{packname}/conditional_formatting_testing.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/einstein.jpg
%doc %{rlibdir}/%{packname}/load_xlsx_testing.R
%doc %{rlibdir}/%{packname}/loadExample.xlsx
%doc %{rlibdir}/%{packname}/namedRegions.xlsx
%doc %{rlibdir}/%{packname}/read_failure_test.xlsx
%doc %{rlibdir}/%{packname}/readTest.xlsx
%doc %{rlibdir}/%{packname}/stack_style_testing.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
