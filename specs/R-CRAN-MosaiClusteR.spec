%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MosaiClusteR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Umbrella Framework for Multi-Source and Multi-Omics Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 

%description
An umbrella framework ("MoSaIC" = Multi-Omics Source-Agnostic Integration
Clustering in R) that unifies a large collection of multi-source /
multi-omics clustering methodologies behind a single, consistent
list-of-matrices interface. It spans five integration paradigms - direct,
similarity-based, graph-based, voting-based consensus, and hierarchy-based
- and bundles a complete downstream workflow for method comparison and
evaluation. The package features the multi-source the ability to compare
many algorithms on the same footing, a data-nugget based feature-weighting
scheme as a robust, big-data-friendly alternative to variance weighting,
and a downstream suite for cluster characterisation, visualisation and
biological interpretation.

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
