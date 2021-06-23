%global __brp_check_rpaths %{nil}
%global packname  PCMBaseCpp
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Likelihood Calculation for Phylogenetic Comparative Models

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-PCMBase 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-PCMBase 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-abind 

%description
Provides a C++ backend for multivariate phylogenetic comparative models
implemented in the R-package 'PCMBase'. Can be used in combination with
'PCMBase' to enable fast and parallel likelihood calculation. Implements
the pruning likelihood calculation algorithm described in Mitov et al.
(2018) <arXiv:1809.09014>. Uses the 'SPLITT' C++ library for parallel tree
traversal described in Mitov and Stadler (2018)
<doi:10.1111/2041-210X.13136>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
