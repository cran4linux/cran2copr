%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbif.range
%global packver   1.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Species Range Mapping from GBIF Using Ecoregion Constraints

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-CoordinateCleaner 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-CoordinateCleaner 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-class 
Requires:         R-CRAN-NMOF 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
A user-friendly, end-to-end workflow to generate ecologically informed
species range maps from sparse observations using environmental clustering
and convex hulls. Serves as a standalone framework or complementary
approach to Species Distribution Models (SDMs). By constraining estimated
ranges within authoritative or custom ecoregion boundaries, the approach
prevents spurious range over-prediction common in geometric hull methods.
The package automates data acquisition via 'GBIF' synonym-aware, tiled
downloads; curates records using 13 configurable filters; and supports
multi-scale analysis by integrating global or user-provided spatial
layers. Also includes disk-based batch processing for large-scale studies
and built-in tools for cross-validation and expert-derived evaluations.

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
