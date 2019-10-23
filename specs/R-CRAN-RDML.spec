%global packname  RDML
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Importing Real-Time Thermo Cycler (qPCR) Data from RDML FormatFiles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-tools >= 3.2
BuildRequires:    R-CRAN-R6 >= 2.0.1
BuildRequires:    R-CRAN-checkmate >= 1.6.2
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-xml2 >= 1.0
BuildRequires:    R-CRAN-rlist >= 0.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
Requires:         R-tools >= 3.2
Requires:         R-CRAN-R6 >= 2.0.1
Requires:         R-CRAN-checkmate >= 1.6.2
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-xml2 >= 1.0
Requires:         R-CRAN-rlist >= 0.4
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pipeR 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 

%description
Imports real-time thermo cycler (qPCR) data from Real-time PCR Data Markup
Language (RDML) and transforms to the appropriate formats of the 'qpcR'
and 'chipPCR' packages. Contains a dendrogram visualization for the
structure of RDML object and GUI for RDML editing.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/RDMLedit
%{rlibdir}/%{packname}/INDEX
