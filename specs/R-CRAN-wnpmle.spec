%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wnpmle
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted NPMLE for Recurrent Events with a Competing Terminal Event

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-TMB >= 1.9.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-TMB >= 1.9.0
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Provides regression modeling and prediction for the marginal mean of
recurrent events in the presence of a competing terminal event using the
weighted nonparametric maximum likelihood estimator (wNPMLE) of Bellach
and Kosorok (2026) <doi:10.48550/arXiv.2605.25934>. Two classes of
transformation models are implemented: Box-Cox transformation models and
logarithmic transformation models. These extend the proportional means
model of Ghosh and Lin (2002) <doi:10.17615/pt0g-y207> and the
transformation model framework of Zeng and Lin (2006)
<doi:10.1093/biomet/93.3.627>. Parameter estimation is performed using
automatic differentiation through the Template Model Builder (TMB)
framework. Standard errors are computed using sandwich variance estimators
that account for estimation of the inverse-probability censoring weights
following Bellach, Kosorok, Rüschendorf and Fine (2019)
<doi:10.1080/01621459.2017.1401540>.

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
