%global packname  Rsampletrees
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          MCMC Sampling of Gene Genealogies Conditional on Genetic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-haplo.stats 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-haplo.stats 
Requires:         R-CRAN-ape 

%description
Sample ancestral trees conditional on phased or unphased SNP genotype
data. The actual tree sampling is done using a C++ program that is
launched within R. The package also contains functions for specifying the
tree-sampling settings (pre-processing) and for storing and manipulating
the sampled trees (post-processing). More information about 'sampletrees'
can be found at <http://stat.sfu.ca/statgen/research/sampletrees.html>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
