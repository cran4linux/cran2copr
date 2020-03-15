%global packname  Ckmeans.1d.dp
%global packver   4.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.2
Release:          1%{?dist}
Summary:          Optimal, Fast, and Reproducible Univariate Clustering

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 

%description
Fast, optimal, and reproducible weighted univariate clustering by dynamic
programming. Four types of problem including univariate k-means, k-median,
k-segments, and multi-channel weighted k-means are solved with guaranteed
optimality and reproducibility. The core algorithm minimizes the sum of
(weighted) within-cluster distances using respective metrics. Its
advantage over heuristic clustering in efficiency and accuracy is
pronounced at a large number of clusters k. Weighted k-means can also
process time series to perform peak calling. Multi-channel weighted
k-means groups multiple univariate signals into k clusters. An auxiliary
function generates histograms that are adaptive to patterns in data. This
package provides a powerful set of tools for univariate data analysis with
guaranteed optimality, efficiency, and reproducibility.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
