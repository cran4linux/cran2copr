%global packname  ClusTorus
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering on the Torus by Conformal Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BAMBI 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-BAMBI 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Provides various tools of for clustering multivariate angular data on the
torus. The package provides angular adaptations of usual clustering
methods such as the k-means clustering, pairwise angular distances, which
can be used as an input for distance-based clustering algorithms, and
implements clustering based on the conformal prediction framework. Options
for the conformal scores include scores based on a kernel density
estimate, multivariate von Mises mixtures, and naive k-means clusters.
Moreover, the package provides some basic data handling tools for angular
data.

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
