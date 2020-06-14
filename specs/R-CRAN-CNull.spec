%global packname  CNull
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Fast Algorithms for Frequency-Preserving Null Models in Ecology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-PhyloMeasures 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-ape 
Requires:         R-CRAN-PhyloMeasures 
Requires:         R-Matrix 

%description
Efficient computations for null models that require shuffling columns on
big matrix data. This package provides functions for faster computation of
diversity measure statistics when independent random shuffling is applied
to the columns of a given matrix. Given a diversity measure f and a matrix
M, the provided functions can generate random samples (shuffled matrix
rows of M), the mean and variance of f, and the p-values of this measure
for two different null models that involve independent random shuffling of
the columns of M. The package supports computations of alpha and beta
diversity measures.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
