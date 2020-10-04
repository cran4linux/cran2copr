%global packname  confreq
%global packver   1.5.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Configural Frequencies Analysis Using Log-Linear Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-gmp 
Requires:         R-methods 

%description
Offers several functions for Configural Frequencies Analysis (CFA), which
is a useful statistical tool for the analysis of multiway contingency
tables. CFA was introduced by G. A. Lienert as 'Konfigurations Frequenz
Analyse - KFA'. Lienert, G. A. (1971). Die Konfigurationsfrequenzanalyse:
I. Ein neuer Weg zu Typen und Syndromen. Zeitschrift für Klinische
Psychologie und Psychotherapie, 19(2), 99–115.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
