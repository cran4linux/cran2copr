%global __brp_check_rpaths %{nil}
%global packname  fitConic
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Data to Any Conic Section

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-pracma 

%description
Fit data to an ellipse, hyperbola, or parabola. Bootstrapping is available
when needed. The conic curve can be rotated through an arbitrary angle and
the fit will still succeed. Helper functions are provided to convert
generator coefficients from one style to another, generate test data sets,
rotate conic section parameters, and so on. References include Nikolai
Chernov (2014) "Fitting ellipses, circles, and lines by least squares"
<https://people.cas.uab.edu/~mosya/cl/>; A. W. Fitzgibbon, M. Pilu, R. B.
Fisher (1999) "Direct Least Squares Fitting of Ellipses" IEEE Trans. PAMI,
Vol. 21, pages 476-48; N. Chernov, Q. Huang, and H. Ma (2014) "Fitting
quadratic curves to data points", British Journal of Mathematics &
Computer Science, 4, 33-60; N. Chernov and H. Ma (2011) "Least squares
fitting of quadratic curves and surfaces", Computer Vision, Editor S. R.
Yoshida, Nova Science Publishers, pp. 285-302.

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
