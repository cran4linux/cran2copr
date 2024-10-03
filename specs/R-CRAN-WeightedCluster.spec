%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WeightedCluster
%global packver   1.8-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering of Weighted Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-TraMineR >= 2.0.6
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-vegclust 
Requires:         R-CRAN-TraMineR >= 2.0.6
Requires:         R-CRAN-cluster 
Requires:         R-utils 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-vegclust 

%description
Clusters state sequences and weighted data. It provides an optimized
weighted PAM algorithm as well as functions for aggregating replicated
cases, computing cluster quality measures for a range of clustering
solutions and plotting (fuzzy) clusters of state sequences. Parametric
bootstraps methods to validate typology of sequences are also provided.
Finally, it provides a fuzzy and crisp CLARA algorithm to cluster large
database with sequence analysis.

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
