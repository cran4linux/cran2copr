%global __brp_check_rpaths %{nil}
%global packname  LSAmitR
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Daten, Beispiele und Funktionen zu 'Large-Scale Assessment mit R'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Hmisc 

%description
Dieses R-Paket stellt Zusatzmaterial in Form von Daten, Funktionen und
R-Hilfe-Seiten für den Herausgeberband Breit, S. und Schreiner, C.
(Hrsg.). (2016). "Large-Scale Assessment mit R: Methodische Grundlagen der
österreichischen Bildungsstandardüberprüfung." Wien: facultas. (ISBN:
978-3-7089-1343-8,
<https://www.iqs.gv.at/themen/bildungsforschung/publikationen/veroeffentlichte-publikationen>)
zur Verfügung.

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
