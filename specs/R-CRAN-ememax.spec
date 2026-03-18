%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ememax
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation for Binary Emax Models with Missing Responses and Bias Reduction

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clinDR >= 2.5.2
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
Requires:         R-CRAN-clinDR >= 2.5.2
Requires:         R-CRAN-BB 
Requires:         R-CRAN-brglm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 

%description
Provides estimation utilities for binary Emax dose-response models.
Includes Expectation-Maximization based maximum likelihood estimation when
the binary response is missing, as well as bias-reduced estimators
including Jeffreys-penalized likelihood, Firth-score, and Cox-Snell
corrections.The methodology is described in Zhang, Pradhan, and Zhao
(2025) <doi:10.1177/09622802251403356> and Zhang, Pradhan, and Zhao (2026)
<doi:10.1080/10543406.2026.2627387>.

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
