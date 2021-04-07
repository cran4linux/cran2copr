%global packname  surf
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survey-Based Gross Flows Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-abind 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-abind 

%description
Estimation of gross flows under non-response and complex sampling designs,
using Gutiérrez, Nascimento Silva and Trujillo (2014)
<https://www150.statcan.gc.ca/n1/pub/12-001-x/2014002/article/14113-eng.pdf>
complex sampling extension of the non-response model developed by Stasny
(1987)
<https://www.scb.se/contentassets/ca21efb41fee47d293bbee5bf7be7fb3/some-markov-chain-models-for-nonresponse-in-estimating-gross-labor-force-flows.pdf>.
It estimates the gross flows process under non-response by modelling the
observable cross-tabulation counts as a two-stage Markov Chain process,
combining (1) the unobservable Markov Chain describing the transition of
states; and (2) the non-response process, given by the initial response
probabilities and the response/non-response transition probabilities.

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
