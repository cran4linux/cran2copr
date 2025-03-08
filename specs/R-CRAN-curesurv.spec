%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  curesurv
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture and Non Mixture Parametric Cure Models to Estimate Cure Indicators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-statmod 

%description
Fits a variety of cure models using excess hazard modeling methodology
such as the mixture model proposed by Phillips et al. (2002)
<doi:10.1002/sim.1101> The Weibull distribution is used to represent the
survival function of the uncured patients; Fits also non-mixture cure
model such as the time-to-null excess hazard model proposed by Boussari et
al. (2020) <doi:10.1111/biom.13361>.

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
