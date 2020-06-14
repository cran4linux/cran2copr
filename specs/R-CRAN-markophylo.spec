%global packname  markophylo
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          2%{?dist}
Summary:          Markov Chain Models for Phylogenetic Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ape >= 3.2
BuildRequires:    R-CRAN-numDeriv >= 2012.9.1
BuildRequires:    R-CRAN-phangorn >= 1.99.13
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape >= 3.2
Requires:         R-CRAN-numDeriv >= 2012.9.1
Requires:         R-CRAN-phangorn >= 1.99.13
Requires:         R-CRAN-Rcpp >= 0.11.4

%description
Allows for fitting of maximum likelihood models using Markov chains on
phylogenetic trees for analysis of discrete character data. Examples of
such discrete character data include restriction sites, gene family
presence/absence, intron presence/absence, and gene family size data.
Hypothesis-driven user- specified substitution rate matrices can be
estimated. Allows for biologically realistic models combining constrained
substitution rate matrices, site rate variation, site partitioning,
branch-specific rates, allowing for non-stationary prior root
probabilities, correcting for sampling bias, etc. See Dang and Golding
(2016) <doi:10.1093/bioinformatics/btv541> for more details.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
