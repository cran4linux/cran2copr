%global packname  HaDeX
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}
Summary:          Analysis and Visualisation of Hydrogen/Deuterium Exchange MassSpectrometry Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Functions for processing, analysis and visualization of Hydrogen Deuterium
eXchange monitored by Mass Spectrometry experiments (HDX-MS). 'HaDeX'
introduces a new standardized and reproducible workflow for the analysis
of the HDX-MS data, including novel uncertainty intervals. Additionally,
it covers data exploration, quality control and generation of
publication-quality figures. All functionalities are also available in the
in-built 'Shiny' app.

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
%doc %{rlibdir}/%{packname}/HaDeX
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
