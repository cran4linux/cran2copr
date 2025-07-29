%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extremeStat
%global packver   1.5.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.11
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Value Statistics and Quantile Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lmomco >= 2.2.5
BuildRequires:    R-CRAN-berryFunctions >= 1.15.6
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-evir 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-fExtremes 
BuildRequires:    R-CRAN-extRemes 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-Renext 
Requires:         R-CRAN-lmomco >= 2.2.5
Requires:         R-CRAN-berryFunctions >= 1.15.6
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-evir 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-fExtremes 
Requires:         R-CRAN-extRemes 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-Renext 

%description
Fit, plot and compare several (extreme value) distribution functions.
Compute (truncated) distribution quantile estimates and plot return
periods on a linear scale. On the fitting method, see Asquith (2011):
Distributional Analysis with L-moment Statistics [...] ISBN 1463508417.

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
