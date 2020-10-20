%global packname  YPmodel
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          The Short-Term and Long-Term Hazard Ratio Model for Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Inference procedures accommodate a flexible range of hazard ratio patterns
with a two-sample semi-parametric model. This model contains the
proportional hazards model and the proportional odds model as sub-models,
and accommodates non-proportional hazards situations to the extreme of
having crossing hazards and crossing survivor functions. Overall, this
package has four major functions: 1) the parameter estimation, namely
short-term and long-term hazard ratio parameters; 2) 95 percent and 90
percent point-wise confidence intervals and simultaneous confidence bands
for the hazard ratio function; 3) p-value of the adaptive weighted
log-rank test; 4) p-values of two lack-of-fit tests for the model. See the
included "read_me_first.pdf" for brief instructions. In this version
(1.1), there is no need to sort the data before applying this package.

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
