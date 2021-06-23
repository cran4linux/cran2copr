%global __brp_check_rpaths %{nil}
%global packname  pmd
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Paired Mass Distance Analysis for GC/LC-MS Based Non-TargetedAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rcdk 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rcdk 
Requires:         R-stats 
Requires:         R-utils 

%description
Paired mass distance (PMD) analysis proposed in Yu, Olkowicz and Pawliszyn
(2018) <doi:10.1016/j.aca.2018.10.062> for gas/liquid chromatography–mass
spectrometry (GC/LC-MS) based non-targeted analysis. PMD analysis
including GlobalStd algorithm and structure/reaction directed analysis.
GlobalStd algorithm could found independent peaks in m/z-retention time
profiles based on retention time hierarchical cluster analysis and
frequency analysis of paired mass distances within retention time groups.
Structure directed analysis could be used to find potential relationship
among those independent peaks in different retention time groups based on
frequency of paired mass distances. A GUI for PMD analysis is also
included as a 'shiny' application.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shinyapp
%{rlibdir}/%{packname}/INDEX
