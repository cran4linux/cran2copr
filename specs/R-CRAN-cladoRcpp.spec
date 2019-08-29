%global packname  cladoRcpp
%global packver   0.15.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.1
Release:          1%{?dist}
Summary:          C++ Implementations of Phylogenetic Cladogenesis Calculations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 

%description
Various cladogenesis-related calculations that are slow in pure R are
implemented in C++ with Rcpp. These include the calculation of the
probability of various scenarios for the inheritance of geographic range
at the divergence events on a phylogenetic tree, and other calculations
necessary for models which are not continuous-time markov chains (CTMC),
but where change instead occurs instantaneously at speciation events.
Typically these models must assess the probability of every possible
combination of (ancestor state, left descendent state, right descendent
state).  This means that there are up to (# of states)^3 combinations to
investigate, and in biogeographical models, there can easily be hundreds
of states, so calculation time becomes an issue.  C++ implementation plus
clever tricks (many combinations can be eliminated a priori) can greatly
speed the computation time over naive R implementations.  CITATION INFO:
This package is the result of my Ph.D. research, please cite the package
if you use it!  Type: citation(package="cladoRcpp") to get the citation
information.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/notes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
