%global packname  EMMIXgene
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          A Mixture Model-Based Approach to the Clustering of MicroarrayExpression Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-stats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-tools 

%description
Provides unsupervised selection and clustering of microarray data using
mixture models. Following the methods described in McLachlan, Bean and
Peel (2002) <doi:10.1093/bioinformatics/18.3.413> a subset of genes are
selected based one the likelihood ratio statistic for the test of one
versus two components when fitting mixtures of t-distributions to the
expression data for each gene. The dimensionality of this gene subset is
further reduced through the use of mixtures of factor analyzers, allowing
the tissue samples to be clustered by fitting mixtures of normal
distributions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
