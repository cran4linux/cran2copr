%global packname  HellCor
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          The Hellinger Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-stats 
Requires:         R-CRAN-energy 
Requires:         R-stats 

%description
Empirical value of the Hellinger correlation, a new measure of dependence
between two continuous random variables that satisfies a set of 7
desirable axioms (existence, symmetry, normalisation, characterisation of
independence, weak Gaussian conformity, characterisation of pure
dependence, generalised Data Processing Inequality). More details can be
found in Geenens and Lafaye De Micheaux (2018) <arXiv:1810.10276>.

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
%doc %{rlibdir}/%{packname}/HISTORY
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
