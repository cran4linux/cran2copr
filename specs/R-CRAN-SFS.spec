%global packname  SFS
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Similarity-First Search Seriation Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.7

%description
An implementation of the Similarity-First Search algorithm (SFS), a
combinatorial algorithm which can be used to solve the seriation problem
and to recognize some structured weighted graphs. The SFS algorithm
represents a generalization to weighted graphs of the graph search
algorithm Lexicographic Breadth-First Search (Lex-BFS), a variant of
Breadth-First Search. The SFS algorithm reduces to Lex-BFS when applied to
binary matrices (or, equivalently, unweighted graphs). Hence this library
can be also considered for Lex-BFS applications such as recognition of
graph classes like chordal or unit interval graphs. In fact, the SFS
seriation algorithm implemented in this package is a multisweep algorithm,
which consists in repeating a finite number of SFS iterations (at most n
sweeps for a matrix of size n). If the data matrix has a Robinsonian
structure, then the ranking returned by the multistep SFS algorithm is a
Robinson ordering of the input matrix. Otherwise the algorithm can be used
as a heuristic to return a ranking partially satisfying the Robinson
property.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
