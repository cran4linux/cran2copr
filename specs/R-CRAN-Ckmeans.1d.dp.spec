%global packname  Ckmeans.1d.dp
%global packver   4.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal, Fast, and Reproducible Univariate Clustering

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rdpack >= 0.6.1
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack >= 0.6.1
Requires:         R-CRAN-Rcpp 

%description
Fast, optimal, and reproducible weighted univariate clustering by dynamic
programming. Four problem are solved, including univariate k-means (Wang &
Song 2011) <doi:10.32614/RJ-2011-015> (Song & Zhong 2020)
<doi:10.1093/bioinformatics/btaa613>, k-median, k-segments, and
multi-channel weighted k-means. Dynamic programming is used to minimize
the sum of (weighted) within-cluster distances using respective metrics.
Its advantage over heuristic clustering in efficiency and accuracy is
pronounced at a large number of clusters. Weighted k-means can also
process time series to perform peak calling. Multi-channel weighted
k-means groups multiple univariate signals into k clusters. An auxiliary
function generates histograms adaptive to patterns in data. This package
provides a powerful set of tools for univariate data analysis with
guaranteed optimality, efficiency, and reproducibility.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
