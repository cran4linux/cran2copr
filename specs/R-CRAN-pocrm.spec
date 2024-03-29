%global __brp_check_rpaths %{nil}
%global packname  pocrm
%global packver   0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Dose Finding in Drug Combination Phase I Trials Using PO-CRM

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dfcrm 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-stats 
Requires:         R-CRAN-dfcrm 
Requires:         R-CRAN-nnet 
Requires:         R-stats 

%description
Provides functions to implement and simulate the partial order continual
reassessment method (PO-CRM) of Wages, Conaway and O'Quigley (2011)
<doi:10.1177/1740774511408748> for use in Phase I trials of combinations
of agents. Provides a function for generating a set of initial guesses
(skeleton) for the toxicity probabilities at each combination that
correspond to the set of possible orderings of the toxicity probabilities
specified by the user.

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
