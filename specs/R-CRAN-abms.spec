%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  abms
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Augmented Bayesian Model Selection for Regression Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-truncnorm 

%description
Tools to perform model selection alongside estimation under Linear,
Logistic, Negative binomial, Quantile, and Skew-Normal regression. Under
the spike-and-slab method, a probability for each possible model is
estimated with the posterior mean, credibility interval, and standard
deviation of coefficients and parameters under the most probable model.

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
