%global packname  DVHmetrics
%global packver   0.3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.10
Release:          2%{?dist}
Summary:          Analyze Dose-Volume Histograms and Check Constraints

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-KernSmooth 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 

%description
Functionality for analyzing dose-volume histograms (DVH) in radiation
oncology: Read DVH text files, calculate DVH metrics as well as
generalized equivalent uniform dose (gEUD), biologically effective dose
(BED), equivalent dose in 2 Gy fractions (EQD2), normal tissue
complication probability (NTCP), and tumor control probability (TCP). Show
DVH diagrams, check and visualize quality assurance constraints for the
DVH. Includes web-based graphical user interface.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/DVHnotebooks
%doc %{rlibdir}/%{packname}/DVHshiny
%{rlibdir}/%{packname}/INDEX
