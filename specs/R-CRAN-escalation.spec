%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  escalation
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          A Modular Approach to Dose-Finding Clinical Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-trialr >= 0.1.5
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-dfcrm 
BuildRequires:    R-CRAN-BOIN 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-trialr >= 0.1.5
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-dfcrm 
Requires:         R-CRAN-BOIN 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-testthat 

%description
Methods for working with dose-finding clinical trials. We provide
implementations of many dose-finding clinical trial designs, including the
continual reassessment method (CRM) by O'Quigley et al. (1990)
<doi:10.2307/2531628>, the toxicity probability interval (TPI) design by
Ji et al. (2007) <doi:10.1177/1740774507079442>, the modified TPI (mTPI)
design by Ji et al. (2010) <doi:10.1177/1740774510382799>, the Bayesian
optimal interval design (BOIN) by Liu & Yuan (2015)
<doi:10.1111/rssc.12089>, EffTox by Thall & Cook (2004)
<doi:10.1111/j.0006-341X.2004.00218.x>; the design of Wages & Tait (2015)
<doi:10.1080/10543406.2014.920873>, and the 3+3 described by Korn et al.
(1994) <doi:10.1002/sim.4780131802>. All designs are implemented with a
common interface. We also offer optional additional classes to tailor the
behaviour of all designs, including avoiding skipping doses, stopping
after n patients have been treated at the recommended dose, stopping when
a toxicity condition is met, or demanding that n patients are treated
before stopping is allowed. By daisy-chaining together these classes using
the pipe operator from 'magrittr', it is simple to tailor the behaviour of
a dose-finding design so it behaves how the trialist wants. Having
provided a flexible interface for specifying designs, we then provide
functions to run simulations and calculate dose-paths for future cohorts
of patients.

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
