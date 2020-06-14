%global packname  WriteXLS
%global packver   5.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.0
Release:          2%{?dist}
Summary:          Cross-Platform Perl Based R Function to Create Excel 2003 (XLS)and Excel 2007 (XLSX) Files

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Cross-platform Perl based R function to create Excel 2003 (XLS) and Excel
2007 (XLSX) files from one or more data frames. Each data frame will be
written to a separate named worksheet in the Excel spreadsheet. The
worksheet name will be the name of the data frame it contains or can be
specified by the user.

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
%doc %{rlibdir}/%{packname}/INSTALL
%doc %{rlibdir}/%{packname}/Perl
%{rlibdir}/%{packname}/INDEX
