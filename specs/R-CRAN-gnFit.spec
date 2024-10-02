%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gnFit
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness of Fit Test for Continuous Distribution Functions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-rmutil 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-rmutil 

%description
Computes the test statistic and p-value of the Cramer-von Mises and
Anderson-Darling test for some continuous distribution functions proposed
by Chen and Balakrishnan (1995)
<http://asq.org/qic/display-item/index.html?item=11407>. In addition to
our classic distribution functions here, we calculate the Goodness of Fit
(GoF) test to dataset which follows the extreme value distribution
function, without remembering the formula of distribution/density
functions. Calculates the Value at Risk (VaR) and Average VaR are another
important risk factors which are estimated by using well-known
distribution functions. Pflug and Romisch (2007, ISBN: 9812707409) is a
good reference to study the properties of risk measures.

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
