%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PPCSexRx
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prescribe Sub-Symptom Exercise for Adolescent Concussion

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-utils 

%description
A clinical decision support system for sub-symptom threshold aerobic
exercise (SSTAE) prescription in adolescents with persistent
post-concussion symptoms (PPCS). Implements an evidence-based protocol
derived from a systematic review of seven studies (Li, 2026;
<doi:10.17605/osf.io/kvuf6>), encoding safety screening, Buffalo
Concussion Treadmill Test (BCTT)-guided heart rate prescription,
session-level progress tracking, and evidence disclosure using the Grading
of Recommendations, Assessment, Development and Evaluation (GRADE)
framework into an open-source tool for athletic trainers and clinicians.
Designed to support implementation in resource-limited settings where BCTT
equipment may be unavailable. GRADE certainty of evidence: LOW. For
clinician use only; not a substitute for clinical judgement.

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
