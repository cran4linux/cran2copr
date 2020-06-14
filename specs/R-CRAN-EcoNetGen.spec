%global packname  EcoNetGen
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Simulate and Sample from Ecological Interaction Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 

%description
Randomly generate a wide range of interaction networks with specified
size, average degree, modularity, and topological structure. Sample nodes
and links from within simulated networks randomly, by degree, by module,
or by abundance. Simulations and sampling routines are implemented in
'FORTRAN', providing efficient generation times even for large networks.
Basic visualization methods also included. Algorithms implemented here are
described in de Aguiar et al. (2017) <arXiv:1708.01242>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/crash.R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
