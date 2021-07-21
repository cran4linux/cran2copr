%global __brp_check_rpaths %{nil}
%global packname  OpenABMCovid19
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Agent-Based Model for Modelling the COVID-19

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xptr 
Requires:         R-CRAN-R6 
Requires:         R-methods 
Requires:         R-CRAN-xptr 

%description
OpenABM-Covid19 is an agent-based model (ABM) developed to simulate the
spread of COVID-19 in a city and to analyse the effect of both passive and
active intervention strategies. Interactions between individuals are
modelled on networks representing households, work-places and random
contacts. The infection is transmitted between these contacts and the
progression of the disease in individuals is modelled. Instantaneous
contract-tracing and quarantining of contacts is modelled allowing the
evaluation of the design and configuration of digital contract-tracing
mobile phone apps. Robert Hinch, William J M Probert, et al. (2020)
<doi:10.1101/2020.09.16.20195925>.

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
