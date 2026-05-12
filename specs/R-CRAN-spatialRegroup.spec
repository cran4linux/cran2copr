%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialRegroup
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Iterative Spatial Regrouping of Administrative Units by Attributive Affinity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rlang 

%description
Evaluates the statistical coherence of existing administrative partitions
(e.g. inter-municipal groupings, districts) by identifying spatial units
whose attributive profile is more similar to a neighbouring group than to
their own. Border units are iteratively reassigned to the group they are
most affine with, based on Euclidean or Mahalanobis distance computed on
user-supplied numeric variables, with optional per-variable weighting and
standardisation. Spatial contiguity is enforced throughout: isolated
candidates are reintegrated into their original group, disconnected
fragments are resolved, and empty groups are restored. Convergence is
monitored via an eta-squared cohesion criterion. The resulting partition
can be compared to the original administrative delineation using
multilevel models, providing a quantitative measure of boundary
inefficiency.

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
