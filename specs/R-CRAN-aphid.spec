%global packname  aphid
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}
Summary:          Analysis with Profile Hidden Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-kmer >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-stats 
Requires:         R-CRAN-kmer >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-graphics 
Requires:         R-CRAN-openssl 
Requires:         R-stats 

%description
Designed for the development and application of hidden Markov models and
profile HMMs for biological sequence analysis. Contains functions for
multiple and pairwise sequence alignment, model construction and parameter
optimization, file import/export, implementation of the forward, backward
and Viterbi algorithms for conditional sequence probabilities, tree-based
sequence weighting, and sequence simulation. Features a wide variety of
potential applications including database searching, gene-finding and
annotation, phylogenetic analysis and sequence classification. Based on
the models and algorithms described in Durbin et al (1998, ISBN:
9780521629713).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
