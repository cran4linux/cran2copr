%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  isotree
%global packver   0.6.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Isolation-Based Outlier Detection

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-jsonlite >= 1.7.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-methods 
Requires:         R-CRAN-jsonlite >= 1.7.3
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-methods 

%description
Fast and multi-threaded implementation of isolation forest (Liu, Ting,
Zhou (2008) <doi:10.1109/ICDM.2008.17>), extended isolation forest
(Hariri, Kind, Brunner (2018) <doi:10.48550/arXiv.1811.02141>), SCiForest
(Liu, Ting, Zhou (2010) <doi:10.1007/978-3-642-15883-4_18>), fair-cut
forest (Cortes (2021) <doi:10.48550/arXiv.2110.13402>), robust random-cut
forest (Guha, Mishra, Roy, Schrijvers (2016)
<http://proceedings.mlr.press/v48/guha16.html>), and customizable
variations of them, for isolation-based outlier detection, clustered
outlier detection, distance or similarity approximation (Cortes (2019)
<doi:10.48550/arXiv.1910.12362>), isolation kernel calculation (Ting, Zhu,
Zhou (2018) <doi:10.1145/3219819.3219990>), and imputation of missing
values (Cortes (2019) <doi:10.48550/arXiv.1911.06646>), based on random or
guided decision tree splitting, and providing different metrics for
scoring anomalies based on isolation depth or density (Cortes (2021)
<doi:10.48550/arXiv.2111.11639>). Provides simple heuristics for fitting
the model to categorical columns and handling missing data, and offers
options for varying between random and guided splits, and for using
different splitting criteria.

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
