%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VOWR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vital Operational Waiting Risk for Healthcare Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survminer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-survminer 

%description
Vital Operational Waiting Risk (VOWR) provides tools for analysing monthly
Referral-to-Treatment (RTT) panel data in healthcare systems. The package
supports provider-level profiling, operational risk classification,
waiting-time volatility assessment, Kaplan-Meier survival analysis, Cox
proportional hazards modelling, and visualisation of time-to-threshold
breach patterns. It is designed to help analysts and decision-makers
identify providers with high waiting times, unstable performance, and
increased risk of earlier threshold breach. The survival modelling methods
follow Cox (1972) <doi:10.1111/j.2517-6161.1972.tb00899.x> and Kaplan and
Meier (1958) <doi:10.1080/01621459.1958.10501452>.

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
