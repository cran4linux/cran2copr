%global __brp_check_rpaths %{nil}
%global packname  ICEinfer
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Incremental Cost-Effectiveness Inference using Two Unbiased Samples

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-lattice 

%description
Given two unbiased samples of patient level data on cost and effectiveness
for a pair of treatments, make head-to-head treatment comparisons by (i)
generating the bivariate bootstrap resampling distribution of ICE
uncertainty for a specified value of the shadow price of health, lambda,
(ii) form the wedge-shaped ICE confidence region with specified confidence
fraction within [0.50, 0.99] that is equivariant with respect to changes
in lambda, (iii) color the bootstrap outcomes within the above confidence
wedge with economic preferences from an ICE map with specified values of
lambda, beta and gamma parameters, (iv) display VAGR and ALICE
acceptability curves, and (v) illustrate variation in ICE preferences by
displaying potentially non-linear indifference(iso-preference) curves from
an ICE map with specified values of lambda, beta and either gamma or eta
parameters.

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
