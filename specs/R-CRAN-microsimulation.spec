%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  microsimulation
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Event Simulation in R and C++, with Tools for Cost-Effectiveness Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ascii 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.10.2
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-grDevices 
Requires:         R-CRAN-ascii 
Requires:         R-CRAN-survival 

%description
Discrete event simulation using both R and C++ (Karlsson et al 2016;
<doi:10.1109/eScience.2016.7870915>). The C++ code is adapted from the
SSIM library <https://www.inf.usi.ch/carzaniga/ssim/>, allowing for
event-oriented simulation. The code includes a SummaryReport class for
reporting events and costs by age and other covariates. The C++ code is
available as a static library for linking to other packages. A priority
queue implementation is given in C++ together with an S3 closure and a
reference class implementation. Finally, some tools are provided for
cost-effectiveness analysis.

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
