%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BRcal
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Boldness-Recalibration of Binary Events

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggplot2 

%description
Boldness-recalibration maximally spreads out probability predictions while
maintaining a user specified level of calibration, facilitated the brcal()
function. Supporting functions to assess calibration via Bayesian and
Frequentist approaches, Maximum Likelihood Estimator (MLE) recalibration,
Linear in Log Odds (LLO)-adjust via any specified parameters, and
visualize results are also provided. Methodological details can be found
in Guthrie & Franck (2024) <doi:10.1080/00031305.2024.2339266>.

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
