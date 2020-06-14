%global packname  LSAmitR
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Daten, Beispiele und Funktionen zu 'Large-Scale Assessment mitR'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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
978-3-7089-1343-8, <https://www.bifie.at/node/3770>) zur Verfügung.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
