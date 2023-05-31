%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LGDtoolkit
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Tools for LGD Rating Model Development

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-monobin 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-monobin 

%description
The goal of this package is to cover the most common steps in Loss Given
Default (LGD) rating model development. The main procedures available are
those that refer to bivariate and multivariate analysis. In particular two
statistical methods for multivariate analysis are currently implemented –
OLS regression and fractional logistic regression. Both methods are also
available within different blockwise model designs and both have
customized stepwise algorithms. Descriptions of these customized designs
are available in Siddiqi (2016) <doi:10.1002/9781119282396.ch10> and
Anderson, R.A. (2021) <doi:10.1093/oso/9780192844194.001.0001>. Although
they are explained for PD model, the same designs are applicable for LGD
model with different underlying regression methods (OLS and fractional
logistic regression). To cover other important steps for LGD model
development, it is recommended to use 'LGDtoolkit' package along with
'PDtoolkit', and 'monobin' (or 'monobinShiny') packages. Additionally,
'LGDtoolkit' provides set of procedures handy for initial and periodical
model validation.

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
