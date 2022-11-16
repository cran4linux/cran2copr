%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LakeMetabolizer
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the Analysis of Ecosystem Metabolism

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-rLakeAnalyzer >= 1.4
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-rLakeAnalyzer >= 1.4
Requires:         R-CRAN-plyr 
Requires:         R-methods 

%description
A collection of tools for the calculation of freewater metabolism from in
situ time series of dissolved oxygen, water temperature, and, optionally,
additional environmental variables. LakeMetabolizer implements 5 different
metabolism models with diverse statistical underpinnings: bookkeeping,
ordinary least squares, maximum likelihood, Kalman filter, and Bayesian.
Each of these 5 metabolism models can be combined with 1 of 7 models for
computing the coefficient of gas exchange across the air–water interface
(k). LakeMetabolizer also features a variety of supporting functions that
compute conversions and implement calculations commonly applied to raw
data prior to estimating metabolism (e.g., oxygen saturation and optical
conversion models).

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
