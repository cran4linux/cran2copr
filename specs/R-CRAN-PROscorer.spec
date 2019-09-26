%global packname  PROscorer
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Functions to Score Commonly-Used Patient-Reported Outcome (PRO)Measures and Other Psychometric Instruments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PROscorerTools 
Requires:         R-CRAN-PROscorerTools 

%description
An extensible repository of accurate, up-to-date functions to score
commonly used patient-reported outcome (PRO), quality of life (QOL), and
other psychometric and psychological measures.  'PROscorer', together with
the 'PROscorerTools' package, is a system to facilitate the incorporation
of PRO measures into research studies and clinical settings in a
scientifically rigorous and reproducible manner.  These packages and their
vignettes are intended to help establish and promote "best practices" to
improve the planning, scoring, and reporting of PRO-like measures in
research. The 'PROscorer' "Instrument Descriptions" vignette contains
descriptions of each instrument scored by 'PROscorer', complete with
references.  These instrument descriptions are suitable for inclusion in
formal study protocol documents, grant proposals, and manuscript Method
sections.  Each 'PROscorer' function is composed of helper functions from
the 'PROscorerTools' package, and users are encouraged to contribute new
functions to 'PROscorer'.  More scoring functions are currently in
development and will be added in future updates.

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
%{rlibdir}/%{packname}/INDEX
