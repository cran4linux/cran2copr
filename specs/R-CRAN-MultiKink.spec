%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiKink
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Inference for Multi-Kink Quantile Regression

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-quantreg 
Requires:         R-methods 
Requires:         R-CRAN-gam 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
Estimation and inference for multiple kink quantile regression for
longitudinal data and the i.i.d data. A bootstrap restarting iterative
segmented quantile algorithm is proposed to estimate the multiple kink
quantile regression model conditional on a given number of change points.
The number of kinks is also allowed to be unknown. In such case, the
backward elimination algorithm and the bootstrap restarting iterative
segmented quantile algorithm are combined to select the number of change
points based on a quantile BIC. For longitudinal data, we also develop the
GEE estimator to incorporate the within-subject correlations.  A
score-type based test statistic is also developed for testing the
existence of kink effect. The package is based on the paper, ``Wei Zhong,
Chuang Wan and Wenyang Zhang (2022). Estimation and inference for
multikink quantile regression, JBES'' and ``Chuang Wan, Wei Zhong, Wenyang
Zhang and Changliang Zou (2022). Multi-kink quantile regression for
longitudinal data with application to progesterone data analysis,
Biometrics".

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
