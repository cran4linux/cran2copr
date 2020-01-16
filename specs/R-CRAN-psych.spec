%global packname  psych
%global packver   1.9.12.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.12.31
Release:          1%{?dist}
Summary:          Procedures for Psychological, Psychometric, and PersonalityResearch

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-nlme 
Requires:         R-CRAN-mnormt 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-nlme 

%description
A general purpose toolbox for personality, psychometric theory and
experimental psychology.  Functions are primarily for multivariate
analysis and scale construction using factor analysis, principal component
analysis, cluster analysis and reliability analysis, although others
provide basic descriptive statistics. Item Response Theory is done using
factor analysis of tetrachoric and polychoric correlations. Functions for
analyzing data at multiple levels include within and between group
statistics, including correlations and factor analysis.  Functions for
simulating and testing particular item and test structures are included.
Several functions serve as a useful front end for structural equation
modeling.  Graphical displays of path diagrams, factor analysis and
structural equation models are created using basic graphics. Some of the
functions are written to support a book on psychometric theory as well as
publications in personality research. For more information, see the
<https://personality-project.org/r> web page.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/News.Rd
%{rlibdir}/%{packname}/INDEX
