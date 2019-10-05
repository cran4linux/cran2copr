%global packname  markovchain
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          Easy Handling Discrete Time Markov Chains

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-stats4 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-expm 
Requires:         R-stats4 
Requires:         R-parallel 
Requires:         R-CRAN-RcppParallel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Functions and S4 methods to create and manage discrete time Markov chains
more easily. In addition functions to perform statistical (fitting and
drawing random variates) and probabilistic (analysis of their structural
proprieties) analysis are provided.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
