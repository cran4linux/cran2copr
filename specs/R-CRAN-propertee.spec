%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  propertee
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Standardization-Based Effect Estimation with Optional Prior Covariance Adjustment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-sandwich 

%description
The Prognostic Regression Offsets with Propagation of ERrors (for
Treatment Effect Estimation) package facilitates direct adjustment for
experiments and observational studies that is compatible with a range of
study designs and covariance adjustment strategies. It uses explicit
specification of clusters, blocks and treatment allocations to furnish
probability of assignment-based weights targeting any of several average
treatment effect parameters, and for standard error calculations
reflecting these design parameters. For covariance adjustment of its Hajek
and (one-way) fixed effects estimates, it enables offsetting the outcome
against predictions from a dedicated covariance model, with standard error
calculations propagating error as appropriate from the covariance model.

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
