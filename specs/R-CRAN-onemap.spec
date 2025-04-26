%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  onemap
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Construction of Genetic Maps in Experimental Crosses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-vcfR >= 1.6.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-princurve 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-rebus 
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-vcfR >= 1.6.0
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-princurve 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-rebus 

%description
Analysis of molecular marker data from model and non-model systems. For
the later, it allows statistical analysis by simultaneously estimating
linkage and linkage phases (genetic map construction) according to Wu and
colleagues (2002) <doi:10.1006/tpbi.2002.1577>. All analysis are based on
multi-point approaches using hidden Markov models.

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
