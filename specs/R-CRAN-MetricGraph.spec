%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MetricGraph
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Fields on Metric Graphs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rSPDE >= 2.3.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-rSPDE >= 2.3.3
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-stats 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggnewscale 

%description
Facilitates creation and manipulation of metric graphs, such as street or
river networks. Further facilitates operations and visualizations of data
on metric graphs, and the creation of a large class of random fields and
stochastic partial differential equations on such spaces. These random
fields can be used for simulation, prediction and inference. In
particular, linear mixed effects models including random field components
can be fitted to data based on computationally efficient sparse matrix
representations. Interfaces to the R packages 'INLA' and 'inlabru' are
also provided, which facilitate working with Bayesian statistical models
on metric graphs. The main references for the methods are Bolin, Simas and
Wallin (2024) <doi:10.3150/23-BEJ1647>, Bolin, Kovacs, Kumar and Simas
(2023) <doi:10.1090/mcom/3929> and Bolin, Simas and Wallin (2023)
<doi:10.48550/arXiv.2304.03190> and <doi:10.48550/arXiv.2304.10372>.

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
