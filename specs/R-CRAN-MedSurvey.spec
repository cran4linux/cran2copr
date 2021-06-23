%global __brp_check_rpaths %{nil}
%global packname  MedSurvey
%global packver   1.1.1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Mediation Analysis for Complex Surveys Using Balanced Repeated Replication

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.50
Requires:         R-core >= 2.50
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-lavaan 
Requires:         R-parallel 

%description
It is a computer tool to conduct linear mediation analysis for complex
surveys using multi-stage sampling and Balanced Repeated Replication
(BRR). Specifically, the mediation analysis method using balanced repeated
replications was proposed by Mai, Ha, and Soulakova (2019)
<DOI:10.1080/10705511.2018.1559065>. The current version can only handle
continuous mediators and outcomes. The development of 'MedSurvey' was
sponsored by American Lebanese Syrian Associated Charities (ALSAC).
However, the contents of MedSurvey do not necessarily represent the policy
of the ALSAC.

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
