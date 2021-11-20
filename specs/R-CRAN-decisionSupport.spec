%global __brp_check_rpaths %{nil}
%global packname  decisionSupport
%global packver   1.109
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.109
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Support of Decision Making under Uncertainty

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-stats >= 3.1.3
BuildRequires:    R-CRAN-nleqslv >= 2.6
BuildRequires:    R-CRAN-rriskDistributions >= 2.0
BuildRequires:    R-CRAN-msm >= 1.5
BuildRequires:    R-CRAN-mvtnorm >= 1.0.2
BuildRequires:    R-CRAN-chillR >= 0.62
BuildRequires:    R-CRAN-fANCOVA >= 0.5
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-stats >= 3.1.3
Requires:         R-CRAN-nleqslv >= 2.6
Requires:         R-CRAN-rriskDistributions >= 2.0
Requires:         R-CRAN-msm >= 1.5
Requires:         R-CRAN-mvtnorm >= 1.0.2
Requires:         R-CRAN-chillR >= 0.62
Requires:         R-CRAN-fANCOVA >= 0.5
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggstance 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
Supporting the quantitative analysis of binary welfare based decision
making processes using Monte Carlo simulations. Decision support is given
on two levels: (i) The actual decision level is to choose between two
alternatives under probabilistic uncertainty. This package calculates the
optimal decision based on maximizing expected welfare. (ii) The meta
decision level is to allocate resources to reduce the uncertainty in the
underlying decision problem, i.e to increase the current information to
improve the actual decision making process. This problem is dealt with
using the Value of Information Analysis. The Expected Value of Information
for arbitrary prospective estimates can be calculated as well as
Individual Expected Value of Perfect Information. The probabilistic
calculations are done via Monte Carlo simulations. This Monte Carlo
functionality can be used on its own.

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
