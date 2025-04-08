%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QR.break
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Breaks in Quantile Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-quantreg 

%description
Methods for detecting structural breaks, determining the number of breaks,
and estimating break locations in linear quantile regression, using one or
multiple quantiles, based on Qu (2008) and Oka and Qu (2011).  Applicable
to both time series and repeated cross-sectional data. The main function
is rq.break().

References for detailed theoretical and empirical explanations:

(1) Qu, Z. (2008). Testing for Structural Change in Regression Quantiles.
Journal of Econometrics, 146(1), 170-184
<doi:10.1016/j.jeconom.2008.08.006>

(2) Oka, T., and Qu, Z. (2011).  Estimating Structural Changes in
Regression Quantiles.  Journal of Econometrics, 162(2), 248-267
<doi:10.1016/j.jeconom.2011.01.005>.

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
