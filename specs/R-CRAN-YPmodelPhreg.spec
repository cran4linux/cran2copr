%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  YPmodelPhreg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Short-Term and Long-Term Hazard Ratio Model with Proportional Adjustment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-survival 

%description
Provides covariate-adjusted comparison of two groups of right censored
data, where the binary group variable has separate short-term and
long-term effects on the hazard function, while effects of covariates such
as age, blood pressure, etc. are proportional on the hazard. The model was
studied in Yang and Prentice (2015) <doi:10.1002/sim.6453> and it extends
the two sample version of the short-term and long-term hazard ratio model
proposed in Yang and Prentice (2005) <doi:10.1093/biomet/92.1.1>. The
model extends the usual Cox proportional hazards model to allow more
flexible hazard ratio patterns, such as gradual onset of effect,
diminishing effect, and crossing hazard or survival functions. This
package provides the following: 1) point estimates and confidence
intervals for model parameters; 2) point estimate and confidence interval
of the average hazard ratio; and 3) plots of estimated hazard ratio
function with point-wise and simultaneous confidence bands.

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
