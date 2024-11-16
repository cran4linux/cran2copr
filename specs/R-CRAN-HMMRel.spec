%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HMMRel
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Markov Models for Reliability and Maintenance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Reliability Analysis and Maintenance Optimization using Hidden Markov
Models (HMM). The use of HMMs to model the state of a system which is not
directly observable and instead certain indicators (signals) of the true
situation are provided via a control system. A hidden model can provide
key information about the system dependability, such as the reliability of
the system and related measures. An estimation procedure is implemented
based on the Baum-Welch algorithm. Classical structures such as K-out-of-N
systems and Shock models are illustrated. Finally, the maintenance of the
system is considered in the HMM context and two functions for new
preventive maintenance strategies are considered. Maintenance efficiency
is measured in terms of expected cost.  Maintenance efficiency is measured
in terms of expected cost. Methods are described in Gamiz, Limnios, and
Segovia-Garcia (2023) <doi:10.1016/j.ejor.2022.05.006>.

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
