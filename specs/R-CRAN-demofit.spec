%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  demofit
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Mortality Curve Fitting and Mortality Forecasting Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-MortalityLaws 
BuildRequires:    R-CRAN-NlcOptim 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-MortalityLaws 
Requires:         R-CRAN-NlcOptim 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Provides tools for fitting parametric mortality curves. Implements
multiple optimisation strategies to enhance robustness and stability of
parameter estimation. Offers tools for forecasting mortality rates guided
by mortality curves. For modelling details see: Tabeau (2001)
<doi:10.1007/0-306-47562-6_1>, Renshaw and Haberman (2006)
<doi:10.1016/j.insmatheco.2005.12.001>, Cairns et al. (2009)
<doi:10.1080/10920277.2009.10597538>, Li and Lee (2005) <doi:
10.1353/dem.2005.0021>.

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
