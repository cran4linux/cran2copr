%global packname  dbscan
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Density Based Clustering of Applications with Noise (DBSCAN) andRelated Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
A fast reimplementation of several density-based algorithms of the DBSCAN
family for spatial data. Includes the DBSCAN (density-based spatial
clustering of applications with noise) and OPTICS (ordering points to
identify the clustering structure) clustering algorithms HDBSCAN
(hierarchical DBSCAN) and the LOF (local outlier factor) algorithm. The
implementations use the kd-tree data structure (from library ANN) for
faster k-nearest neighbor search. An R interface to fast kNN and
fixed-radius NN search is also provided. See Hahsler M, Piekenbrock M and
Doran D (2019) <doi:10.18637/jss.v091.i01>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/test_data
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
