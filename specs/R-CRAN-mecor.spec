%global __brp_check_rpaths %{nil}
%global packname  mecor
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Measurement Error Correction in Linear Models with a Continuous Outcome

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-numDeriv 

%description
Covariate measurement error correction is implemented by means of
regression calibration by Carroll RJ, Ruppert D, Stefanski LA &
Crainiceanu CM (2006, ISBN:1584886331), efficient regression calibration
by Spiegelman D, Carroll RJ & Kipnis V (2001)
<doi:10.1002/1097-0258(20010115)20:1%%3C139::AID-SIM644%%3E3.0.CO;2-K> and
maximum likelihood estimation by Bartlett JW, Stavola DBL & Frost C (2009)
<doi:10.1002/sim.3713>. Outcome measurement error correction is
implemented by means of the method of moments by Buonaccorsi JP (2010,
ISBN:1420066560) and efficient method of moments by Keogh RH, Carroll RJ,
Tooze JA, Kirkpatrick SI & Freedman LS (2014) <doi:10.1002/sim.7011>.
Standard error estimation of the corrected estimators is implemented by
means of the Delta method by Rosner B, Spiegelman D & Willett WC (1990)
<doi:10.1093/oxfordjournals.aje.a115715> and Rosner B, Spiegelman D &
Willett WC (1992) <doi:10.1093/oxfordjournals.aje.a116453>, the Fieller
method described by Buonaccorsi JP (2010, ISBN:1420066560), and the
Bootstrap by Carroll RJ, Ruppert D, Stefanski LA & Crainiceanu CM (2006,
ISBN:1584886331).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
