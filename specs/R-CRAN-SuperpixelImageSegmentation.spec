%global __brp_check_rpaths %{nil}
%global packname  SuperpixelImageSegmentation
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Superpixel Image Segmentation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-OpenImageR 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-ClusterR 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-R6 
Requires:         R-CRAN-OpenImageR 
Requires:         R-grDevices 
Requires:         R-CRAN-lattice 

%description
Image Segmentation using Superpixels, Affinity Propagation and Kmeans
Clustering. The R code is based primarily on the article "Image
Segmentation using SLIC Superpixels and Affinity Propagation Clustering,
Bao Zhou, International Journal of Science and Research (IJSR), 2013"
<https://www.ijsr.net/archive/v4i4/SUB152869.pdf>.

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
