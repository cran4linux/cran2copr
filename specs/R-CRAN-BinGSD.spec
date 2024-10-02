%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BinGSD
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Boundaries and Conditional Power for Single Arm Group Sequential Test with Binary Endpoint

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
Requires:         R-methods >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-mvtnorm >= 1.0.11

%description
Consider an at-most-K-stage group sequential design with only an upper
bound for the last analysis and non-binding lower bounds.With binary
endpoint, two kinds of test can be applied, asymptotic test based on
normal distribution and exact test based on binomial distribution. This
package supports the computation of boundaries and conditional power for
single-arm group sequential test with binary endpoint, via either
asymptotic or exact test. The package also provides functions to obtain
boundary crossing probabilities given the design.

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
