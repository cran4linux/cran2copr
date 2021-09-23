%global __brp_check_rpaths %{nil}
%global packname  Clustering
%global packver   1.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Techniques for Evaluating Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-advclust 
BuildRequires:    R-CRAN-amap 
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-advclust 
Requires:         R-CRAN-amap 
Requires:         R-CRAN-apcluster 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sqldf 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xtable 

%description
The design of this package allows us to run different clustering packages
and compare the results between them, to determine which algorithm behaves
best from the data provided.

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
