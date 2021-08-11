%global __brp_check_rpaths %{nil}
%global packname  autoMFA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithms for Automatically Fitting MFA Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-expm 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-usethis 

%description
Provides methods for fitting the Mixture of Factor Analyzers (MFA) model
automatically. The MFA model is a mixture model where each sub-population
is assumed to follow the Factor Analysis model. The Factor Analysis (FA)
model is a latent variable model which assumes that observations are
normally distributed, but imposes constraints on their covariance matrix.
The MFA model contains two hyperparameters; g (the number of components in
the mixture) and q (the number of factors in each component Factor
Analysis model). Usually, the Expectation-Maximisation algorithm would be
used to fit the MFA model, but this requires g and q to be known. This
package treats g and q as unknowns and provides several methods which
infer these values with as little input from the user as possible.

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
