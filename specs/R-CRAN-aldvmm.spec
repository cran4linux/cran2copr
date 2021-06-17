%global packname  aldvmm
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Adjusted Limited Dependent Variable Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-optimr 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-optimr 

%description
The goal of the package 'aldvmm' is to fit adjusted limited dependent
variable mixture models of health state utilities. Adjusted limited
dependent variable mixture models are finite mixtures of normal
distributions with an accumulation of density mass at the limits, and a
gap between 100%% quality of life and the next smaller utility value. The
package 'aldvmm' uses the likelihood and expected value functions proposed
by Hernandez Alava and Wailoo (2015) <doi:10.1177/1536867X1501500307>
using normal component distributions and a multinomial logit model of
probabilities of component membership.

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
