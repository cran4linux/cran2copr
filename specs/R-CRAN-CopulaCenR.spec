%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CopulaCenR
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Copula-Based Regression Models for Multivariate Censored Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-icenReg 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-survival 

%description
Copula-based regression models for multivariate censored data, including
bivariate right-censored data, bivariate interval-censored data, and
interval-censored semi-competing risks data. Currently supports Clayton,
Gumbel, Frank, Joe, AMH and Copula2 copula models. For marginal models, it
supports parametric (Weibull, Loglogistic, Gompertz) and semiparametric
(Cox and transformation) models. Includes methods for convenient
prediction and plotting. Also provides a bivariate time-to-event
simulation function. Method details can be found in Sun et.al (2019)
Lifetime Data Analysis, Sun et.al (2021) Biostatistics, and Sun et.al
(2022) Statistical Methods in Medical Research.

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
