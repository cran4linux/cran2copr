%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  accrual
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Accrual Prediction

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-fgui 
BuildRequires:    R-CRAN-SMPracticals 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-fgui 
Requires:         R-CRAN-SMPracticals 

%description
Participant recruitment for medical research is challenging. Slow accrual
leads to delays in research. Accrual monitoring during the process of
recruitment is critical. Researchers need reliable tools to manage the
accrual rate. We developed a Bayesian method that integrates the
researcher's experience with previous trials and data from the current
study, providing reliable predictions on accrual rate for clinical
studies. For more details and background on these methodologies, see the
publications of Byron, Stephen and Susan (2008) <doi:10.1002/sim.3128>,
and Yu et al. (2015) <doi:10.1002/sim.6359>. In this R package, Bayesian
accrual prediction functions are presented, which can be easily used by
statisticians and clinical researchers.

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
