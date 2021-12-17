%global __brp_check_rpaths %{nil}
%global packname  midas2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Drug-Combination Platform Design(MIDAS-2)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-R2jags 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-R2jags 

%description
Implementation of Bayesian drug-combination platform design. More and more
immuno-oncology drug combinations make the traditional two-arm phase II
trials inefficient, which stimulate the emerge of platform trials. In the
case of multiple trial objectives such as candidates screening and
subgroup analysis, we propose an information borrowing drug-combination
Bayesian design for platform trials with subgroup exploration. MIDAS-2
consists of one control arm and several experimental agents. We use
Bayesian spike and slab prior to identify factors that should be included
in regression model and borrow information between combinations in the
existence of subgroup interaction. Promising drug combinations are allowed
to graduated early to move to next stage and new combination strategies
can be added accordingly. Catch-up rule, curtail rule and early stopping
rules are also applied to accelerate the trial process.

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
