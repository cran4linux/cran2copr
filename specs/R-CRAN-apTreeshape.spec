%global packname  apTreeshape
%global packver   1.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          2%{?dist}
Summary:          Analyses of Phylogenetic Treeshape

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-pbapply 

%description
Simulation and analysis of phylogenetic tree topologies using statistical
indices. It is a companion library of the 'ape' package. It provides
additional functions for reading, plotting, manipulating phylogenetic
trees. It also offers convenient web-access to public databases, and
enables testing null models of macroevolution using corrected test
statistics.  Trees of class "phylo" (from 'ape' package) can be converted
easily. Implements methods described in Bortolussi et al. (2005)
<doi:10.1093/bioinformatics/bti798> and Maliet et al. (2017)
<doi:10.1101/224295>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
