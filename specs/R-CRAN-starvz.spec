%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  starvz
%global packver   0.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          R-Based Visualization Techniques for Task-Based Applications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-Rcpp >= 1.0.6

%description
Performance analysis workflow that combines the power of the R language
(and the tidyverse realm) and many auxiliary tools to provide a
consistent, flexible, extensible, fast, and versatile framework for the
performance analysis of task-based applications that run on top of the
StarPU runtime (with its MPI (Message Passing Interface) layer for
multi-node support).  Its goal is to provide a fruitful prototypical
environment to conduct performance analysis hypothesis-checking for
task-based applications that run on heterogeneous (multi-GPU, multi-core)
multi-node HPC (High-performance computing) platforms.

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
