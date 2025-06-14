%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  graphicalExtremes
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methodology for Graphical Extreme Value Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-igraph >= 1.2.4.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.10
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-CRAN-CVXR 
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-igraph >= 1.2.4.1
Requires:         R-CRAN-mvtnorm >= 1.0.10
Requires:         R-CRAN-Rdpack 
Requires:         R-utils 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-glassoFast 
Requires:         R-CRAN-CVXR 

%description
Statistical methodology for sparse multivariate extreme value models.
Methods are provided for exact simulation and statistical inference for
multivariate Pareto distributions on graphical structures as described in
the paper 'Graphical Models for Extremes' by Engelke and Hitz (2020)
<doi:10.1111/rssb.12355>.

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
