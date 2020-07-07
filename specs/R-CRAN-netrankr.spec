%global packname  netrankr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Analyzing Partial Rankings in Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.8

%description
Implements methods for centrality related analyses of networks. While the
package includes the possibility to build more than 20 indices, its main
focus lies on index-free assessment of centrality via partial rankings
obtained by neighborhood-inclusion or positional dominance. These partial
rankings can be analyzed with different methods, including probabilistic
methods like computing expected node ranks and relative rank probabilities
(how likely is it that a node is more central than another?). The
methodology is described in depth in the vignettes and in Schoch (2018)
<doi:10.1016/j.socnet.2017.12.003>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
