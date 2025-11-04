%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  barrel
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Covariance-Based Ellipses and Annotation Tools for Ordination Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-vegan 
Requires:         R-grid 
Requires:         R-CRAN-rlang 

%description
Provides tools to visualize ordination results in 'R' by adding
covariance-based ellipses, centroids, vectors, and confidence regions to
plots created with 'ggplot2'. The package extends the 'vegan' framework
and supports Principal Component Analysis (PCA), Redundancy Analysis
(RDA), and Non-metric Multidimensional Scaling (NMDS). Ellipses can
represent either group dispersion (standard deviation, SD) or centroid
precision (standard error, SE), following Wang et al. (2015)
<doi:10.1371/journal.pone.0118537>. Robust estimators of covariance are
implemented, including the Minimum Covariance Determinant (MCD) method of
Hubert et al. (2018) <doi:10.1002/wics.1421>. This approach reduces the
influence of outliers. barrel is particularly useful for multivariate
ecological datasets, promoting reproducible, publication-quality
ordination graphics with minimal effort.

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
