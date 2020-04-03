%global packname  PINSPlus
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Clustering Algorithm for Data Integration and Disease Subtyping

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-FNN 
Requires:         R-cluster 

%description
Provides a robust approach for omics data integration and disease
subtyping. 'PINSPlus' supports both single and multiple data types. The
software automatically determines the optimal number of clusters and then
partitions the samples in a way such that the results are robust to noise
and data perturbation (Hung Nguyen (2018)
<doi:10.1093/bioinformatics/bty1049>, Tin Nguyen (2017)
<doi:10.1101/gr.215129.116>). 'PINSPlus' is fast and it supports parallel
computing on Windows, Linux, and Mac OS.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
