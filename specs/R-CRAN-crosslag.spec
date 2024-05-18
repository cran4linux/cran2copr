%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crosslag
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Linear or Nonlinear Cross Lag Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 6.8.0
BuildRequires:    R-stats >= 4.3.2
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-utils >= 3.1.0
BuildRequires:    R-CRAN-mgcv >= 1.9.1
BuildRequires:    R-CRAN-lavaan >= 0.6.17
BuildRequires:    R-CRAN-ggpubr >= 0.6.0
BuildRequires:    R-CRAN-gamm4 >= 0.2.6
Requires:         R-CRAN-rms >= 6.8.0
Requires:         R-stats >= 4.3.2
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-utils >= 3.1.0
Requires:         R-CRAN-mgcv >= 1.9.1
Requires:         R-CRAN-lavaan >= 0.6.17
Requires:         R-CRAN-ggpubr >= 0.6.0
Requires:         R-CRAN-gamm4 >= 0.2.6

%description
Linear or nonlinear cross-lagged panel model can be built from input data.
Users can choose the appropriate method from three methods for
constructing nonlinear cross lagged models. These three methods include
polynomial regression, generalized additive model and generalized linear
mixed model.In addition, a function for determining linear relationships
is provided. Relevant knowledge of cross lagged models can be learned
through the paper by Fredrik Falkenström (2024)
<doi:10.1016/j.cpr.2024.102435> and the paper by A Gasparrini (2010)
<doi:10.1002/sim.3940>.

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
