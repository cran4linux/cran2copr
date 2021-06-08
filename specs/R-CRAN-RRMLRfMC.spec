%global packname  RRMLRfMC
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reduced-Rank Multinomial Logistic Regression for Markov Chains

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-nnet 

%description
Fit the reduced-rank multinomial logistic regression model for Markov
chains developed by Wang, Abner, Fardo, Schmitt, Jicha, Eldik and Kryscio
(2021)<doi:10.1002/sim.8923> in R. It combines the ideas of multinomial
logistic regression in Markov chains and reduced-rank. It is very useful
in a study where multi-states model is assumed and each transition among
the states is controlled by a series of covariates. The key advantage is
to reduce the number of parameters to be estimated. The final coefficients
for all the covariates and the p-values for the interested covariates will
be reported. The p-values for the whole coefficient matrix can be
calculated by two bootstrap methods.

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
