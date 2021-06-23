%global __brp_check_rpaths %{nil}
%global packname  micEcon
%global packver   0.6-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.16
Release:          1%{?dist}%{?buildtag}
Summary:          Microeconomic Analysis and Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plm >= 1.1.0
BuildRequires:    R-CRAN-miscTools >= 0.6.1
Requires:         R-CRAN-plm >= 1.1.0
Requires:         R-CRAN-miscTools >= 0.6.1

%description
Various tools for microeconomic analysis and microeconomic modelling, e.g.
estimating quadratic, Cobb-Douglas and Translog functions, calculating
partial derivatives and elasticities of these functions, and calculating
Hessian matrices, checking curvature and preparing restrictions for
imposing monotonicity of Translog functions.

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
