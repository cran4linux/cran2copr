%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survPhenoStab
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stability-Driven Hierarchical Clustering for Multi-Endpoint Survival Phenotyping

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
Requires:         R-CRAN-mclust 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 

%description
Implements the stability-driven hierarchical clustering framework for
multi-endpoint patient phenotyping described in Roy Chowdhury et al., "A
stability-driven hierarchical clustering framework for multi-endpoint
patient phenotyping in oncology" (submitted to Computers in Biology and
Medicine). Provides survival feature-space embedding for multiple
time-to-event endpoints, a competing-risks data-generating mechanism for
simulation, an exhaustive sweep over valid distance-linkage-K
configurations, bootstrap Jaccard cluster-stability assessment, a
chaining- artefact diagnostic (Delta_CA), cluster-number selection
combining silhouette width, the gap statistic and bootstrap stability, and
benchmarking against k-means and Gaussian mixture models.

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
