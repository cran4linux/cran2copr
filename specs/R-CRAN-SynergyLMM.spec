%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SynergyLMM
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Framework for in Vivo Drug Combination Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-nlme >= 3.1.165
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-cowplot >= 1.1.3
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-nlmeU 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-marginaleffects 
BuildRequires:    R-CRAN-clubSandwich 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-nlme >= 3.1.165
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-cowplot >= 1.1.3
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-nlmeU 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-car 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-marginaleffects 
Requires:         R-CRAN-clubSandwich 

%description
A framework for evaluating drug combination effects in preclinical in vivo
studies. 'SynergyLMM' provides functions to analyze longitudinal tumor
growth experiments using mixed-effects models, perform time-resolved
analyses of synergy and antagonism, evaluate model diagnostics and
performance, and assess both post-hoc and a priori statistical power. The
calculation of drug combination synergy follows the statistical framework
provided by Demidenko and Miller (2019,
<doi:10.1371/journal.pone.0224137>). The implementation and analysis of
linear mixed-effect models is based on the methods described by Pinheiro
and Bates (2000, <doi:10.1007/b98882>), and Gałecki and Burzykowski (2013,
<doi:10.1007/978-1-4614-3900-4>).

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
