%global packname  walkr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Random Walks in the Intersection of Hyperplanes and theN-Simplex

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.6
BuildRequires:    R-CRAN-hitandrun 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-shinystan 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.6
Requires:         R-CRAN-hitandrun 
Requires:         R-CRAN-limSolve 
Requires:         R-MASS 
Requires:         R-CRAN-shinystan 

%description
Consider the intersection of two spaces: the complete solution space to Ax
= b and the N-simplex. The intersection of these two spaces is a
non-negative convex polytope. The package walkr samples from this
intersection using two Monte-Carlo Markov Chain (MCMC) methods:
hit-and-run and Dikin walk. walkr also provide tools to examine sample
quality. The package implements Dikin walk specified in Sachdeva (2016)
<doi:10.1016/j.orl.2016.07.005>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
