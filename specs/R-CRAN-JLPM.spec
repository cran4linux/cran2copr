%global __brp_check_rpaths %{nil}
%global packname  JLPM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Latent Process Models

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-survival >= 2.37.2
BuildRequires:    R-CRAN-marqLevAlg >= 2.0.6
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-survival >= 2.37.2
Requires:         R-CRAN-marqLevAlg >= 2.0.6
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-stringr 

%description
Estimation of extended joint models with shared random effects.
Longitudinal data are handled in latent process models for continuous
(Gaussian or curvilinear) and ordinal outcomes while proportional hazard
models are used for the survival part. We propose a frequentist approach
using maximum likelihood estimation. See Saulnier et al, 2021
<arXiv:2110.02612>.

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
