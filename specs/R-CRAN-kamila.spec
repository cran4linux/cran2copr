%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kamila
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Clustering Mixed-Type Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-Rcpp 

%description
Implements methods for clustering mixed-type data, specifically
combinations of continuous and nominal data. Special attention is paid to
the often-overlooked problem of equitably balancing the contribution of
the continuous and categorical variables. This package implements KAMILA
clustering, a novel method for clustering mixed-type data in the spirit of
k-means clustering. It does not require dummy coding of variables, and is
efficient enough to scale to rather large data sets. Also implemented is
Modha-Spangler clustering, which uses a brute-force strategy to maximize
the cluster separation simultaneously in the continuous and categorical
variables. For more information, see Foss, Markatou, Ray, & Heching (2016)
<doi:10.1007/s10994-016-5575-7> and Foss & Markatou (2018)
<doi:10.18637/jss.v083.i13>.

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
