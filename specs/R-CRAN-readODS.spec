%global packname  readODS
%global packver   1.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.7
Release:          1%{?dist}
Summary:          Read and Write ODS Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringi 

%description
Import ODS (OpenDocument Spreadsheet) into R as a data frame. Also support
writing data frame into ODS file.

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
%doc %{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/INDEX
