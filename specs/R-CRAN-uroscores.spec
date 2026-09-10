%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  uroscores
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scoring Tools for Urology and Pelvic Health Research Instruments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Scores standardized patient-reported instruments used in urology and
pelvic health research, including the International Prostate Symptom Score
(Barry et al., 1992), the Overactive Bladder Symptom Score (Homma et al.,
2006) <doi:10.1016/j.urology.2006.02.042>, the O'Leary-Sant interstitial
cystitis indices, the short forms of the Urogenital Distress Inventory and
the Incontinence Impact Questionnaire (Uebersax et al., 1995)
<doi:10.1002/nau.1930140206>, the Sandvik incontinence severity index, and
the Benign Prostatic Hyperplasia Impact Index. Instruments are declarative
definitions read by a single scoring engine. Responses are checked against
the permitted value set of each item, missing items follow the published
rule for the instrument or return NA when none was published, severity
bands are assigned by membership, and published minimal important
difference statistics are included for responder analyses.

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
