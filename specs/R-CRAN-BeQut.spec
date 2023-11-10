%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BeQut
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation for Quantile Regression Mixed Models

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-jagsUI 
BuildRequires:    R-CRAN-lqmm 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-jagsUI 
Requires:         R-CRAN-lqmm 
Requires:         R-CRAN-MASS 

%description
Using a Bayesian estimation procedure, this package fits linear quantile
regression models such as linear quantile models, linear quantile mixed
models, quantile regression joint models for time-to-event and
longitudinal data. The estimation procedure is based on the asymmetric
Laplace distribution and the 'JAGS' software is used to get posterior
samples (Yang, Luo, DeSantis (2019) <doi:10.1177/0962280218784757>).

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
