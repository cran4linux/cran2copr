%global packname  Ckmeans.1d.dp
%global packver   4.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.2
Release:          1%{?dist}
Summary:          Optimal and Fast Univariate Clustering

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Fast optimal univariate clustering and segementation by dynamic
programming. Three types of problem including univariate k-means,
k-median, and k-segments are solved with guaranteed optimality and
reproducibility. The core algorithm minimizes the sum of within-cluster
distances using respective metrics. Its advantage over heuristic
clustering algorithms in efficiency and accuracy is increasingly
pronounced as the number of clusters k increases. Weighted k-means and
unweighted k-segments algorithms can also optimally segment time series
and perform peak calling. An auxiliary function generates histograms that
are adaptive to patterns in data. In contrast to heuristic methods, this
package provides a powerful set of tools for univariate data analysis with
guaranteed optimality. Use four spaces when indenting paragraphs within
the Description.

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
