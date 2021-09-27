%global __brp_check_rpaths %{nil}
%global packname  stochQN
%global packver   0.1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Limited Memory Quasi-Newton Optimizers

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Implementations of stochastic, limited-memory quasi-Newton optimizers,
similar in spirit to the LBFGS (Limited-memory
Broyden-Fletcher-Goldfarb-Shanno) algorithm, for smooth stochastic
optimization. Implements the following methods: oLBFGS (online LBFGS)
(Schraudolph, N.N., Yu, J. and Guenter, S., 2007
<http://proceedings.mlr.press/v2/schraudolph07a.html>), SQN (stochastic
quasi-Newton) (Byrd, R.H., Hansen, S.L., Nocedal, J. and Singer, Y., 2016
<arXiv:1401.7020>), adaQN (adaptive quasi-Newton) (Keskar, N.S., Berahas,
A.S., 2016, <arXiv:1511.01169>). Provides functions for easily creating R
objects with partial_fit/predict methods from some given
objective/gradient/predict functions. Includes an example stochastic
logistic regression using these optimizers. Provides header files and
registered C routines for using it directly from C/C++.

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
