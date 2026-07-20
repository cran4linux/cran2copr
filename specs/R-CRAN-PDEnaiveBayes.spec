%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PDEnaiveBayes
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plausible Naive Bayes Classifier Using PDE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-RcppParallel >= 5.1.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DatabionicSwarm 
BuildRequires:    R-CRAN-memshare 
Requires:         R-CRAN-RcppParallel >= 5.1.4
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-plotly 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DatabionicSwarm 
Requires:         R-CRAN-memshare 

%description
Provides a nonparametric, multicore-capable plausible naive Bayes
classifier based on Pareto density estimation (PDE). It addresses
low-evidence cases through a plausibility correction. To enhance the
interpretability of the flexible naive Bayes classifier by revealing its
posterior structure and feature-wise, class-specific evidence, posterior
probabilities can be visualized as class-wise line plots for
one-dimensional data or color-coded Voronoi diagrams for pairwise feature
projections, and class-conditional PDE likelihoods as overlaid, mirrored
density profiles resembling violin plots. Methodological details are
provided by Stier, Q., Hoffmann, J. and Thrun, M. C. (2026) "Classifying
with the Fine Structure of Distributions: Leveraging Distributional
Information for Robust and Plausible Naive Bayes"
<DOI:10.3390/make8010013>. For multicore computations, the implementation
applies the general memory-sharing approach described by Thrun, M. C. and
Märte, J. (2026) "memshare: Memory Sharing for Multicore Computation in R
with an Application to Feature Selection by Mutual Information using PDE"
<DOI:10.32614/RJ-2025-043>.

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
