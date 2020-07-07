%global packname  popprxl
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          Read GenAlEx Files Directly from Excel

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-poppr >= 2.0.2
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-utils 
Requires:         R-CRAN-poppr >= 2.0.2
Requires:         R-CRAN-readxl 
Requires:         R-utils 

%description
GenAlEx is a popular Excel macro for genetic analysis and the 'poppr' R
package allows import of GenAlEx formatted CSV data for genetic data
analysis in R. This package allows for the import of GenAlEx formatted
Excel files, serving as a small 'poppr' add on for those who have trouble
or simply do not want to export their data into CSV format.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/files
%{rlibdir}/%{packname}/INDEX
