%global packname  multimark
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          2%{?dist}
Summary:          Capture-Mark-Recapture Analysis using Multiple Non-InvasiveMarks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-RMark 
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-RMark 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 

%description
Traditional and spatial capture-mark-recapture analysis with multiple
non-invasive marks. The models implemented in 'multimark' combine
encounter history data arising from two different non-invasive ``marks'',
such as images of left-sided and right-sided pelage patterns of
bilaterally asymmetrical species, to estimate abundance and related
demographic parameters while accounting for imperfect detection. Bayesian
models are specified using simple formulae and fitted using Markov chain
Monte Carlo. Addressing deficiencies in currently available software,
'multimark' also provides a user-friendly interface for performing
Bayesian multimodel inference using non-spatial or spatial
capture-recapture data consisting of a single conventional mark or
multiple non-invasive marks.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
