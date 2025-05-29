%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  outlierMBC
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Outlier Identification for Model-Based Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-flexCWM 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mixture 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-spatstat.univar 
BuildRequires:    R-stats 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-flexCWM 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mixture 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-spatstat.univar 
Requires:         R-stats 

%description
Sequential outlier identification for Gaussian mixture models using the
distribution of Mahalanobis distances. The optimal number of outliers is
chosen based on the dissimilarity between the theoretical and observed
distributions of the scaled squared sample Mahalanobis distances. Also
includes an extension for Gaussian linear cluster-weighted models using
the distribution of studentized residuals. Doherty, McNicholas, and White
(2025) <doi:10.48550/arXiv.2505.11668>.

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
