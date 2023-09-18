%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MKclass
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Classification

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Performance measures and scores for statistical classification such as
accuracy, sensitivity, specificity, recall, similarity coefficients, AUC,
GINI index, Brier score and many more. Calculation of optimal cut-offs and
decision stumps (Iba and Langley (1991),
<doi:10.1016/B978-1-55860-247-2.50035-8>) for all implemented performance
measures. Hosmer-Lemeshow goodness of fit tests (Lemeshow and Hosmer
(1982), <doi:10.1093/oxfordjournals.aje.a113284>; Hosmer et al (1997),
<doi:10.1002/(SICI)1097-0258(19970515)16:9%%3C965::AID-SIM509%%3E3.0.CO;2-O>).
Statistical and epidemiological risk measures such as relative risk, odds
ratio, number needed to treat (Porta (2014),
<doi:10.1093%%2Facref%%2F9780199976720.001.0001>).

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
