%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppwdeming
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Precision Profile Weighted Deming Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Weighted Deming regression, also known as 'errors-in-variable' regression,
is applied with suitable weights. Weights are modeled via a precision
profile; thus the methods implemented here are referred to as precision
profile weighted Deming (PWD) regression. The package covers two settings
– one where the precision profiles are known either from external studies
or from adequate replication of the X and Y readings, and one in which
there is a plausible functional form for the precision profiles but the
exact (unknown) function must be estimated from the (generally singlicate)
readings. The function set includes tools for: estimated standard errors
(via jackknifing); standardized-residual analysis function with regression
diagnostic tools for normality, linearity and constant variance; and an
outlier analysis identifying significant outliers for closer
investigation. The following reference provides further information on
mathematical derivations and applications. Hawkins, D.M., and J.J. Kraker.
'Precision Profile Weighted Deming Regression for Methods Comparison', (in
press) <doi:10.1093/jalm/jfaf183>.

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
