%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lmw
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Model Weights

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 3.0.2
BuildRequires:    R-CRAN-backports >= 1.4.1
BuildRequires:    R-CRAN-chk >= 0.9.1
Requires:         R-CRAN-sandwich >= 3.0.2
Requires:         R-CRAN-backports >= 1.4.1
Requires:         R-CRAN-chk >= 0.9.1

%description
Computes the implied weights of linear regression models for estimating
average causal effects and provides diagnostics based on these weights.
These diagnostics rely on the analyses in Chattopadhyay and Zubizarreta
(2023) <doi:10.1093/biomet/asac058> where several regression estimators
are represented as weighting estimators, in connection to inverse
probability weighting. 'lmw' provides tools to diagnose
representativeness, balance, extrapolation, and influence for these
models, clarifying the target population of inference. Tools are also
available to simplify estimating treatment effects for specific target
populations of interest.

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
