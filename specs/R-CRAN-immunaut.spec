%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  immunaut
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Immunogenicity and Vaccine Response Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-PRROC 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-clusterSim 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Used for analyzing immune responses and predicting vaccine efficacy using
machine learning and advanced data processing techniques. 'Immunaut'
integrates both unsupervised and supervised learning methods, managing
outliers and capturing immune response variability. It performs multiple
rounds of predictive model testing to identify robust immunogenicity
signatures that can predict vaccine responsiveness. The platform is
designed to handle high-dimensional immune data, enabling researchers to
uncover immune predictors and refine personalized vaccination strategies
across diverse populations.

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
