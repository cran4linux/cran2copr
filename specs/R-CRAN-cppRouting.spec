%global packname  cppRouting
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Fast Implementation of Dijkstra Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-data.table 

%description
Calculation of distances, shortest paths and isochrones on weighted graphs
using several variants of Dijkstra algorithm. Proposed algorithms are
unidirectional Dijkstra (Dijkstra, E. W. (1959) <doi:10.1007/BF01386390>),
bidirectional Dijkstra (Goldberg, Andrew & Fonseca F. Werneck, Renato
(2005)
<https://pdfs.semanticscholar.org/0761/18dfbe1d5a220f6ac59b4de4ad07b50283ac.pdf>),
A* search (P. E. Hart, N. J. Nilsson et B. Raphael (1968)
<doi:10.1109/TSSC.1968.300136>), new bidirectional A* (Pijls & Post (2009)
<http://repub.eur.nl/pub/16100/ei2009-10.pdf>), Contraction hierarchies
(R. Geisberger, P. Sanders, D. Schultes and D. Delling (2008)
<doi:10.1007/978-3-540-68552-4_24>), PHAST (D. Delling, A.Goldberg, A.
Nowatzyk, R. Werneck (2011) <doi:10.1016/j.jpdc.2012.02.007>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
