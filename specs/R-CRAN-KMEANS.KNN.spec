%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KMEANS.KNN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          KMeans and KNN Clustering Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-class 
Requires:         R-CRAN-caret 
Requires:         R-grDevices 

%description
Implementation of Kmeans clustering algorithm and a supervised KNN (K
Nearest Neighbors) learning method. It allows users to perform
unsupervised clustering and supervised classification on their datasets.
Additional features include data normalization, imputation of missing
values, and the choice of distance metric. The package also provides
functions to determine the optimal number of clusters for Kmeans and the
best k-value for KNN: knn_Function(), find_Knn_best_k(),
KMEANS_FUNCTION(), and find_Kmeans_best_k().

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
