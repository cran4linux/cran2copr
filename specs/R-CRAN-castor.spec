%global packname  castor
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          2%{?dist}
Summary:          Efficient Phylogenetics on Large Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-naturalsort 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-parallel 
Requires:         R-CRAN-naturalsort 
Requires:         R-stats 
Requires:         R-CRAN-nloptr 

%description
Efficient phylogenetic analyses on massive phylogenies comprising up to
millions of tips. Functions include pruning, rerooting, calculation of
most-recent common ancestors, calculating distances from the tree root and
calculating pairwise distances. Calculation of phylogenetic signal and
mean trait depth (trait conservatism), ancestral state reconstruction and
hidden character prediction of discrete characters, simulating and fitting
models of trait evolution, fitting and simulating diversification models,
dating trees, comparing trees, and reading/writing trees in Newick format.
Citation: Louca, Stilianos and Doebeli, Michael (2017)
<doi:10.1093/bioinformatics/btx701>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
