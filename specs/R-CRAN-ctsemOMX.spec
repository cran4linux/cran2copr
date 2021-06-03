%global packname  ctsemOMX
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Time SEM - 'OpenMx' Based Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ctsem >= 3.3.2
BuildRequires:    R-CRAN-OpenMx >= 2.9.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ctsem >= 3.3.2
Requires:         R-CRAN-OpenMx >= 2.9.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Original 'ctsem' (continuous time structural equation modelling)
functionality, based on the 'OpenMx' software, as described in Driver,
Oud, Voelkle (2017) <doi:10.18637/jss.v077.i05>, with updated details in
vignette. Combines stochastic differential equations representing latent
processes with structural equation measurement models. These functions
were split off from the main package of 'ctsem', as the main package uses
the 'rstan' package as a backend now -- offering estimation options from
max likelihood to Bayesian. There are nevertheless use cases for the wide
format SEM style approach as offered here, particularly when there are no
individual differences in observation timing and the number of individuals
is large. For the main 'ctsem' package, see
<https://cran.r-project.org/package=ctsem>.

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
