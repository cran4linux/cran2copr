%global __brp_check_rpaths %{nil}
%global packname  opGMMassessment
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Optimized Automated Gaussian Mixture Assessment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AdaptGauss 
BuildRequires:    R-CRAN-DataVisualizations 
BuildRequires:    R-CRAN-DistributionOptimization 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mixAK 
BuildRequires:    R-CRAN-multimode 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-AdaptGauss 
Requires:         R-CRAN-DataVisualizations 
Requires:         R-CRAN-DistributionOptimization 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mixtools 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mixAK 
Requires:         R-CRAN-multimode 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-doParallel 

%description
Necessary functions for optimized automated evaluation of the number and
parameters of Gaussian mixtures in one-dimensional data. Various methods
are available for parameter estimation and for determining the number of
modes in the mixture.

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
