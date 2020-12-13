%global packname  dominanceanalysis
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dominance Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
Dominance analysis is a method that allows to compare the relative
importance of predictors in multiple regression models: ordinary least
squares, generalized linear models, hierarchical linear models, beta
regression and dynamic linear models. The main principles and methods of
dominance analysis are described in Budescu, D. V. (1993)
<doi:10.1037/0033-2909.114.3.542> and Azen, R., & Budescu, D. V. (2003)
<doi:10.1037/1082-989X.8.2.129> for ordinary least squares regression.
Subsequently, the extensions for multivariate regression, logistic
regression and hierarchical linear models were described in Azen, R., &
Budescu, D. V. (2006) <doi:10.3102/10769986031002157>, Azen, R., & Traxel,
N. (2009) <doi:10.3102/1076998609332754> and Luo, W., & Azen, R. (2013)
<doi:10.3102/1076998612458319>, respectively.

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
