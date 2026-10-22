%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boundedHill
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Logistic Regression with Lower and Upper Asymptotes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-stats 
Requires:         R-CRAN-BayesLogit 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-posterior 
Requires:         R-stats 

%description
Fits Bayesian logistic regression models in which the success probability
rises or falls between a lower and an upper asymptote instead of between 0
and 1, for binomial outcomes including binary data. The success
probability equals the lower asymptote plus the difference between the two
asymptotes multiplied by the logistic function of a linear predictor. The
lower and upper asymptotes can be either estimated or fixed. With a single
predictor such as log dose, this is the four-parameter logistic (Hill)
model. Posterior computation is a full Gibbs sampler that requires no
tuning.

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
