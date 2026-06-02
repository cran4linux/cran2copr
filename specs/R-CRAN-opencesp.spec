%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  opencesp
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generation and Evaluation of Synthetic Tabular Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fastmap 
BuildRequires:    R-CRAN-PCAmixdata 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-mice 
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-rpart 
Requires:         R-parallel 
Requires:         R-CRAN-fastmap 
Requires:         R-CRAN-PCAmixdata 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-mice 

%description
Various tools developed as part of the Open-CESP (Centre de recherche en
Epidémiologie et Santé des Populations) initiative to generate and
evaluate synthetic datasets for statistical disclosure control. This
includes tools to investigate the risk-utility tradeoff achievable with
given synthesis methods, as well as statistical tools to estimate
(conditional) probability distributions. The main eventual aim is to help
researchers and statisticians disseminate open research data.

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
