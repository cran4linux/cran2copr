%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FPDclustering
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          PD-Clustering and Related Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ThreeWay 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ExPosition 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggeasy 
Requires:         R-CRAN-ThreeWay 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ExPosition 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggeasy 

%description
Probabilistic distance clustering (PD-clustering) is an iterative,
distribution free, probabilistic clustering method. PD-clustering assigns
units to a cluster according to their probability of membership, under the
constraint that the product of the probability and the distance of each
point to any cluster centre is a constant. PD-clustering is a flexible
method that can be used with non-spherical clusters, outliers, or noisy
data. PDQ is an extension of the algorithm for clusters of different size.
GPDC and TPDC uses a dissimilarity measure based on densities. Factor
PD-clustering (FPDC) is a factor clustering method that involves a linear
transformation of variables and a cluster optimizing the PD-clustering
criterion. It works on high dimensional data sets.

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
