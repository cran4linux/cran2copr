%global packname  OptCirClust
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Circular, Periodic, or Framed Data Clustering: Fast, Optimal, and Reproducible

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Ckmeans.1d.dp 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Ckmeans.1d.dp 
Requires:         R-graphics 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Fast, optimal, and reproducible clustering algorithms for circular,
periodic, or framed data. The algorithms introduced in this package are
based on a core optimal framed clustering algorithm. The runtime of these
algorithms is O(K N log^2 N), where K is the number of clusters and N is
the number of circular data points. On a desktop computer using a single
processor core, millions of circular data points can be clustered within
seconds. One can use the algorithms to characterize events along circular
DNA molecules, circular RNA molecules, and circular genomes of bacteria,
chloroplast, and mitochondria. One can also cluster climate data along any
given longitude or latitude. Periodic data clustering can be formulated as
circular clustering. The algorithms offer a general high-performance
solution to circular, periodic, or framed data clustering.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
