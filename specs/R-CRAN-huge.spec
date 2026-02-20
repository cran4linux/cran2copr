%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  huge
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Undirected Graph Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Provides a general framework for high-dimensional undirected graph
estimation. It integrates data preprocessing, neighborhood screening,
graph estimation, and model selection techniques into a pipeline. In
preprocessing stage, the nonparanormal(npn) transformation is applied to
help relax the normality assumption. In the graph estimation stage, the
graph structure is estimated by Meinshausen-Buhlmann graph estimation or
the graphical lasso, and both methods can be further accelerated by the
lossy screening rule preselecting the neighborhood of each variable by
correlation thresholding. We target on high-dimensional data analysis
usually d >> n, and the computation is memory-optimized using the sparse
matrix output. We also provide a computationally efficient approach,
correlation thresholding graph estimation. Three
regularization/thresholding parameter selection methods are included in
this package: (1)stability approach for regularization selection (2)
rotation information criterion (3) extended Bayesian information criterion
which is only available for the graphical lasso.

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
