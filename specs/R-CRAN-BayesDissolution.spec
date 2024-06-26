%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesDissolution
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Models for Dissolution Testing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-shiny 
Requires:         R-stats 

%description
Fits Bayesian models (amongst others) to dissolution data sets that can be
used for dissolution testing. The package was originally constructed to
include only the Bayesian models outlined in Pourmohamad et al. (2022)
<doi:10.1111/rssc.12535>. However, additional Bayesian and non-Bayesian
models (based on bootstrapping and generalized pivotal quanties) have also
been added. More models may be added over time.

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
