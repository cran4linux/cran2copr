%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qqkrls
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile-on-Quantile Kernel Regularized Least Squares

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.0.0
BuildRequires:    R-CRAN-KRLS >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-CRAN-KRLS >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Implements Quantile-on-Quantile Kernel-Based Regularized Least Squares
(QQKRLS) as in Adebayo, Ozkan and Eweade (2024)
<doi:10.1016/j.jclepro.2024.140832>. Combines Kernel-Based Regularized
Least Squares (KRLS) of Hainmueller and Hazlett (2014)
<doi:10.1093/pan/mpt019> with the Quantile-on-Quantile regression of Sim
and Zhou (2015) <doi:10.1016/j.jbankfin.2015.01.013>: for each quantile
theta of the independent variable the response is fit by KRLS on the
corresponding sub-sample and the tau-quantile of the resulting pointwise
marginal effects yields beta(theta, tau). Standard errors come from a
paired bootstrap. Visualisations use the 'MATLAB' 'Parula' colour map by
default.

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
