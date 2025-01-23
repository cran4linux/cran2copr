%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  presmoothedTP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Presmoothed Landmark Aalen-Johansen Estimator of Transition Probabilities for Complex Multi-State Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mstate 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mstate 
Requires:         R-CRAN-plyr 

%description
Multi-state models are essential tools in longitudinal data analysis. One
primary goal of these models is the estimation of transition
probabilities, a critical metric for predicting clinical prognosis across
various stages of diseases or medical conditions. Traditionally, inference
in multi-state models relies on the Aalen-Johansen (AJ) estimator which is
consistent under the Markov assumption. However, in many practical
applications, the Markovian nature of the process is often not guaranteed,
limiting the applicability of the AJ estimator in more complex scenarios.
This package extends the landmark Aalen-Johansen estimator (Putter, H,
Spitoni, C (2018) <doi:10.1177/0962280216674497>) incorporating
presmoothing techniques described by Soutinho, Meira-Machado and Oliveira
(2020) <doi:10.1080/03610918.2020.1762895>, offering a robust alternative
for estimating transition probabilities in non-Markovian multi-state
models with multiple states and potential reversible transitions.

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
