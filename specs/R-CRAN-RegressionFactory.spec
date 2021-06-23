%global __brp_check_rpaths %{nil}
%global packname  RegressionFactory
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Expander Functions for Generating Full Gradient and Hessian from Single-Slot and Multi-Slot Base Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The expander functions rely on the mathematics developed for the
Hessian-definiteness invariance theorem for linear projection
transformations of variables, described in authors' paper, to generate the
full, high-dimensional gradient and Hessian from the lower-dimensional
derivative objects. This greatly relieves the computational burden of
generating the regression-function derivatives, which in turn can be fed
into any optimization routine that utilizes such derivatives. The theorem
guarantees that Hessian definiteness is preserved, meaning that reasoning
about this property can be performed in the low-dimensional space of the
base distribution. This is often a much easier task than its equivalent in
the full, high-dimensional space. Definiteness of Hessian can be useful in
selecting optimization/sampling algorithms such as Newton-Raphson
optimization or its sampling equivalent, the Stochastic Newton Sampler.
Finally, in addition to being a computational tool, the regression
expansion framework is of conceptual value by offering new opportunities
to generate novel regression problems.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
