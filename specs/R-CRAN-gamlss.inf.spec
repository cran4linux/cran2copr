%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gamlss.inf
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Mixed (Inflated and Adjusted) Distributions

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.1
Requires:         R-core >= 2.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-methods 

%description
This is an add-on package to 'gamlss'. The purpose of this package is to
allow users to fit GAMLSS (Generalised Additive Models for Location Scale
and Shape) models when the response variable is defined either in the
intervals [0,1), (0,1] and [0,1] (inflated at zero and/or one
distributions), or in the positive real line including zero (zero-adjusted
distributions). The mass points at zero and/or one are treated as extra
parameters with the possibility to include a linear predictor for both.
The package also allows transformed or truncated distributions from the
GAMLSS family to be used for the continuous part of the distribution.
Standard methods and GAMLSS diagnostics can be used with the resulting
fitted object.

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
