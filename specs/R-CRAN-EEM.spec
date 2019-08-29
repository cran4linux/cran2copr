%global packname  EEM
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Read and Preprocess Fluorescence Excitation-Emission Matrix(EEM) Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-tools 
Requires:         R-CRAN-reshape2 
Requires:         R-graphics 
Requires:         R-CRAN-colorRamps 
Requires:         R-utils 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ggplot2 

%description
Read raw EEM data and prepares them for further analysis.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
