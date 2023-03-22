%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qgraph
%global packver   1.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Graph Plotting Methods, Psychometric Data Visualization and Graphical Model Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-gtools 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-abind 

%description
Fork of qgraph - Weighted network visualization and analysis, as well as
Gaussian graphical model computation. See Epskamp et al. (2012)
<doi:10.18637/jss.v048.i04>.

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
