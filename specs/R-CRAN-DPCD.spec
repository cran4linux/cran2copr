%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPCD
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dirichlet Process Clustering with Dissimilarities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-mcclust 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-nimble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-mcclust 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-truncnorm 

%description
A Bayesian hierarchical model for clustering dissimilarity data using the
Dirichlet process. The latent configuration of objects and the number of
clusters are automatically inferred during the fitting process. The
package supports multiple models which are available to detect clusters of
various shapes and sizes using different covariance structures. Additional
functions are included to ensure adequate model fits through prior and
posterior predictive checks.

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
