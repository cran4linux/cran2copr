%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crm12Comb
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Phase I/II CRM Based Drug Combination Design

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 

%description
Implements the adaptive designs for integrated phase I/II trials of drug
combinations via continual reassessment method (CRM) to evaluate toxicity
and efficacy simultaneously for each enrolled patient cohort based on
Bayesian inference. It supports patients assignment guidance in a single
trial using current enrolled data, as well as conducting extensive
simulation studies to evaluate operating characteristics before the trial
starts. It includes various link functions such as empiric, one-parameter
logistic, two-parameter logistic, and hyperbolic tangent, as well as
considering multiple prior distributions of the parameters like normal
distribution, gamma distribution and exponential distribution to
accommodate diverse clinical scenarios. Method using Bayesian framework
with empiric link function is described in: Wages and Conaway (2014)
<doi:10.1002/sim.6097>.

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
