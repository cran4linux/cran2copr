%global packname  genie
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          A New, Fast, and Outlier Resistant Hierarchical ClusteringAlgorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-stats 

%description
A new hierarchical clustering linkage criterion: the Genie algorithm links
two clusters in such a way that a chosen economic inequity measure (e.g.,
the Gini index) of the cluster sizes does not increase drastically above a
given threshold. Benchmarks indicate a high practical usefulness of the
introduced method: it most often outperforms the Ward or average linkage
in terms of the clustering quality while retaining the single linkage
speed, see (Gagolewski et al. 2016a <DOI:10.1016/j.ins.2016.05.003>, 2016b
<DOI:10.1007/978-3-319-45656-0_16>) for more details.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
