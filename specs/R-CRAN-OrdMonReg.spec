%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OrdMonReg
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Least Squares Estimates of One Bounded or Two Ordered Isotonic Regression Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
We consider the problem of estimating two isotonic regression curves g1*
and g2* under the constraint that they are ordered, i.e. g1* <= g2*. Given
two sets of n data points y_1, ..., y_n and z_1, ..., z_n that are
observed at (the same) deterministic design points x_1, ..., x_n, the
estimates are obtained by minimizing the Least Squares criterion L(a, b) =
sum_{i=1}^n (y_i - a_i)^2 w1(x_i) + sum_{i=1}^n (z_i - b_i)^2 w2(x_i) over
the class of pairs of vectors (a, b) such that a and b are isotonic and
a_i <= b_i for all i = 1, ..., n. We offer two different approaches to
compute the estimates: a projected subgradient algorithm where the
projection is calculated using a PAVA as well as Dykstra's cyclical
projection algorithm.

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
