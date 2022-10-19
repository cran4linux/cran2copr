%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  np
%global packver   0.60-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.60.16
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Kernel Smoothing Methods for Mixed Data Types

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-cubature 
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-quantreg 
Requires:         R-stats 

%description
Nonparametric (and semiparametric) kernel methods that seamlessly handle a
mix of continuous, unordered, and ordered factor data types. We would like
to gratefully acknowledge support from the Natural Sciences and
Engineering Research Council of Canada (NSERC,
<https://www.nserc-crsng.gc.ca/>), the Social Sciences and Humanities
Research Council of Canada (SSHRC, <https://www.sshrc-crsh.gc.ca/>), and
the Shared Hierarchical Academic Research Computing Network (SHARCNET,
<https://sharcnet.ca/>). We would also like to acknowledge the
contributions of the GNU GSL authors. In particular, we adapt the GNU GSL
B-spline routine gsl_bspline.c adding automated support for quantile knots
(in addition to uniform knots), providing missing functionality for
derivatives, and for extending the splines beyond their endpoints.

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
