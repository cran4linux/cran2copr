%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sjSDM
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Joint Species Distribution Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-beeswarm 
BuildRequires:    R-CRAN-qgam 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Metrics 
Requires:         R-parallel 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-beeswarm 
Requires:         R-CRAN-qgam 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-viridis 

%description
A scalable and fast method for estimating joint Species Distribution
Models (jSDMs) for big community data, including eDNA data. The package
estimates a full (i.e. non-latent) jSDM with different response
distributions (including the traditional multivariate probit model). The
package allows to perform variation partitioning (VP) / ANOVA on the
fitted models to separate the contribution of environmental, spatial, and
biotic associations. In addition, the total R-squared can be further
partitioned per species and site to reveal the internal metacommunity
structure, see Leibold et al., <doi:10.1111/oik.08618>. The internal
structure can then be regressed against environmental and spatial
distinctiveness, richness, and traits to analyze metacommunity assembly
processes.  The package includes support for accounting for spatial
autocorrelation and the option to fit responses using deep neural networks
instead of a standard linear predictor. As described in Pichler & Hartig
(2021) <doi:10.1111/2041-210X.13687>, scalability is achieved by using a
Monte Carlo approximation of the joint likelihood implemented via
'PyTorch' and 'reticulate', which can be run on CPUs or GPUs.

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
