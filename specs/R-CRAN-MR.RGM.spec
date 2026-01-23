%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MR.RGM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Multivariate Bidirectional Mendelian Randomization Networks Using Bayesian Directed Cyclic Graphical Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-GIGrvg 

%description
Addressing a central challenge encountered in Mendelian randomization (MR)
studies, where MR primarily focuses on discerning the effects of
individual exposures on specific outcomes and establishes causal links
between them. Using a network-based methodology, the intricacy involving
interdependent outcomes due to numerous factors has been tackled through
this routine. Based on Ni et al. (2018) <doi:10.1214/17-BA1087>, 'MR.RGM'
extends to a broader exploration of the causal landscape by leveraging on
network structures and involves the construction of causal graphs that
capture interactions between response variables and consequently between
responses and instrument variables. The resulting Graph visually
represents these causal connections, showing directed edges with effect
sizes labeled. 'MR.RGM' facilitates the navigation of various data
availability scenarios effectively by accommodating three input formats,
i.e., individual-level data and two types of summary-level data. The
method also optionally incorporates measured covariates (when available)
and allows flexible modeling of the error variance structure, including
correlated errors that may reflect unmeasured confounding among responses.
In the process, causal effects, adjacency matrices, and other essential
parameters of the complex biological networks, are estimated. Besides,
'MR.RGM' provides uncertainty quantification for specific network
structures among response variables. Parts of the Inverse Wishart sampler
are adapted from the econ722 repository by DiTraglia (GPL-2.0).

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
