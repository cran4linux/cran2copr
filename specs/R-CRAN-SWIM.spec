%global __brp_check_rpaths %{nil}
%global packname  SWIM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scenario Weights for Importance Measurement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
An efficient sensitivity analysis for stochastic models based on Monte
Carlo samples. Provides weights on simulated scenarios from a stochastic
model, such that stressed random variables fulfil given probabilistic
constraints (e.g. specified values for risk measures), under the new
scenario weights. Scenario weights are selected by constrained
minimisation of the relative entropy to the baseline model. The 'SWIM'
package is based on Pesenti S.M., Millossovich P., Tsanakas A. (2019)
"Reverse Sensitivity Testing: What does it take to break the model"
<openaccess.city.ac.uk/id/eprint/18896/> and Pesenti S.M. (2021) "Reverse
Sensitivity Analysis for Risk Modelling"
<https://www.ssrn.com/abstract=3878879>.

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
