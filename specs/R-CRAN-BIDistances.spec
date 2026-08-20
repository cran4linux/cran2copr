%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BIDistances
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bioinformatic Distances

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-parallelDist 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-DataVisualizations 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-RcppParallel >= 5.1.1
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-parallelDist 
Requires:         R-parallel 
Requires:         R-CRAN-DataVisualizations 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 

%description
Provides a unified interface for computing, comparing, and examining
distances, dissimilarities, divergences, and selected similarities for
bioinformatics data. The core installation exposes 60 canonical named
routes for numerical data and more than 90 when the suggested
'philentropy' backend is installed; aliases, user-defined functions, and
mixed-data combinations are not included in these counts. Weighted
Minkowski distances can be computed through 'parallelDist', an internal
multicore implementation, or optional 'OpenCL' kernels, while the
established weighted Euclidean GPU implementation is retained as the
optimized p = 2 route. The package also supports theory-guided comparison
of distance distributions for clustering, explicit mathematical property
classifications, mixed-data constructions through 'manydist', and a
specialized Gene Ontology-derived TF-IDF distance.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
