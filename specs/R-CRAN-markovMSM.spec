%global __brp_check_rpaths %{nil}
%global packname  markovMSM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Checking the Markov Condition in Multi-State Survival Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survidm 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mstate 
Requires:         R-CRAN-survidm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mstate 

%description
The inference in multi-state models is traditionally performed under a
Markov assumption that claims that past and future of the process are
independent given the present state. In this package, we consider tests of
the Markov assumption that are applicable to general multi-state models.
Three approaches using existing methodology are considered: a simple
method based on including covariates depending on the history in Cox
models for the transition intensities; methods based on measuring the
discrepancy of the non-Markov estimators of the transition probabilities
to the Markov Aalen-Johansen estimators; and, finally, methods that were
developed by considering summaries from families of log-rank statistics
where patients are grouped by the state occupied of the process at a
particular time point (see Soutinho G, Meira-Machado L (2021)
<doi:10.1007/s00180-021-01139-7> and Titman AC, Putter H (2020)
<doi:10.1093/biostatistics/kxaa030>).

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
