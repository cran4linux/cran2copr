%global packname  lqr
%global packver   3.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.31
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Linear Quantile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MomTrunc 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MomTrunc 
Requires:         R-CRAN-quantreg 

%description
It fits a robust linear quantile regression model using a new family of
zero-quantile distributions for the error term. Missing values and
censored observations can be handled as well. This family of distribution
includes skewed versions of the Normal, Student's t, Laplace, Slash and
Contaminated Normal distribution. It also performs logistic quantile
regression for bounded responses as shown in Galarza et.al.(2020)
<doi:10.1007/s13571-020-00231-0>. It provides estimates and full
inference. It also provides envelopes plots for assessing the fit and
confidences bands when several quantiles are provided simultaneously.

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
