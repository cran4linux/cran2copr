%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cureAssess
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Cure Model Appropriateness for Survival Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-flexsurvcure 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-flexsurvcure 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
Assesses whether cure models are appropriate for right-censored survival
data, where a fraction of subjects may never experience the event of
interest. Implements a two-stage workflow combining Kaplan-Meier
visualization and comparison of parametric cure and non-cure models by the
Akaike information criterion with formal diagnostics for sufficient
follow-up and for the presence of a cured fraction. The diagnostics
include the statistics of Maller and Zhou (1992)
<doi:10.1093/biomet/79.4.731> and Maller and Zhou (1994)
<doi:10.1080/01621459.1994.10476889>, the test of Shen (2000)
<doi:10.1016/S0167-7152(00)00063-8>, and the ratio estimation of censored
uncured subjects ('RECeUS') method of Selukar and Othus (2023)
<doi:10.1002/sim.9610>.

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
