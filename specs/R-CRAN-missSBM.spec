%global packname  missSBM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Handling Missing Data in Stochastic Block Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-magrittr 

%description
When a network is partially observed (here, NAs in the adjacency matrix
rather than 1 or 0 due to missing information between node pairs), it is
possible to account for the underlying process that generates those NAs.
'missSBM' adjusts the popular stochastic block model from network data
sampled under various missing data conditions, as described in Tabouy,
Barbillon and Chiquet (2019) <doi:10.1080/01621459.2018.1562934>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/covariates.R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
