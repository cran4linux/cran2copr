%global __brp_check_rpaths %{nil}
%global packname  EmiR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Evolutionary Minimizer for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-plot3D 
Requires:         R-graphics 

%description
A C++ implementation of the following evolutionary algorithms: Bat
Algorithm (Yang, 2010 <doi:10.1007/978-3-642-12538-6_6>), Cuckoo Search
(Yang, 2009 <doi:10.1109/nabic.2009.5393690>), Genetic Algorithms
(Holland, 1992, ISBN:978-0262581110), Gravitational Search Algorithm
(Rashedi et al., 2009 <doi:10.1016/j.ins.2009.03.004>), Grey Wolf
Optimization (Mirjalili et al., 2014
<doi:10.1016/j.advengsoft.2013.12.007>), Harmony Search (Geem et al., 2001
<doi:10.1177/003754970107600201>), Improved Harmony Search (Mahdavi et
al., 2007 <doi:10.1016/j.amc.2006.11.033>), Moth-flame Optimization
(Mirjalili, 2015 <doi:10.1016/j.knosys.2015.07.006>), Particle Swarm
Optimization (Kennedy et al., 2001 ISBN:1558605959), Simulated Annealing
(Kirkpatrick et al., 1983 <doi:10.1126/science.220.4598.671>), Whale
Optimization Algorithm (Mirjalili and Lewis, 2016
<doi:10.1016/j.advengsoft.2016.01.008>). 'EmiR' can be used not only for
unconstrained optimization problems, but also in presence of inequality
constrains, and variables restricted to be integers.

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
