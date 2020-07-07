%global packname  dtwclust
%global packver   5.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.5.6
Release:          3%{?dist}
Summary:          Time Series Clustering Along with Optimizations for the DynamicTime Warping Distance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-RcppParallel >= 4.4.0
BuildRequires:    R-CRAN-proxy >= 0.4.16
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-RcppParallel >= 4.4.0
Requires:         R-CRAN-proxy >= 0.4.16
Requires:         R-methods 
Requires:         R-CRAN-dtw 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-clue 
Requires:         R-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-Matrix 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Time series clustering along with optimized techniques related to the
Dynamic Time Warping distance and its corresponding lower bounds.
Implementations of partitional, hierarchical, fuzzy, k-Shape and TADPole
clustering are available. Functionality can be easily extended with custom
distance measures and centroid definitions. Implementations of DTW
barycenter averaging, a distance based on global alignment kernels, and
the soft-DTW distance and centroid routines are also provided. All
included distance functions have custom loops optimized for the
calculation of cross-distance matrices, including parallelization support.
Several cluster validity indices are included.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/interactive-clustering
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/ssdtwclust
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
