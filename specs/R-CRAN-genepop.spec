%global packname  genepop
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          Population Genetic Data Analysis Using Genepop

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-stringr 

%description
Makes the Genepop software available in R. This software implements a
mixture of traditional population genetic methods and some more focused
developments: it computes exact tests for Hardy-Weinberg equilibrium, for
population differentiation and for genotypic disequilibrium among pairs of
loci; it computes estimates of F-statistics, null allele frequencies,
allele size-based statistics for microsatellites, etc.; and it performs
analyses of isolation by distance from pairwise comparisons of individuals
or population samples.

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
%doc %{rlibdir}/%{packname}/application.yml
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Dockerfile
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/extdoc
%doc %{rlibdir}/%{packname}/genepop-shiny
%doc %{rlibdir}/%{packname}/make-exe
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/Rprofile.site
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
