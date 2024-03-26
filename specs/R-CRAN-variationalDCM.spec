%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  variationalDCM
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Bayesian Estimation for Diagnostic Classification Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Enables computationally efficient parameters-estimation by variational
Bayesian methods for various diagnostic classification models (DCMs). DCMs
are a class of discrete latent variable models for classifying respondents
into latent classes that typically represent distinct combinations of
skills they possess. Recently, to meet the growing need of large-scale
diagnostic measurement in the field of educational, psychological, and
psychiatric measurements, variational Bayesian inference has been
developed as a computationally efficient alternative to the Markov chain
Monte Carlo methods, e.g., Yamaguchi and Okada (2020a)
<doi:10.1007/s11336-020-09739-w>, Yamaguchi and Okada (2020b)
<doi:10.3102/1076998620911934>, Yamaguchi (2020)
<doi:10.1007/s41237-020-00104-w>, Oka and Okada (2023)
<doi:10.1007/s11336-022-09884-4>, and Yamaguchi and Martinez (2023)
<doi:10.1111/bmsp.12308>. To facilitate their applications,
'variationalDCM' is developed to provide a collection of recently-proposed
variational Bayesian estimation methods for various DCMs.

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
