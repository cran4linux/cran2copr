%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LactCurveModels
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Lactation Curve Model Fitting for Dairy Animals

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Fits up to 20 nonlinear lactation curve models to dairy animal milk yield
data. Models fitted include exponential, polynomial, mixed logarithmic,
inverse polynomial, and sigmoid families published between 1923 and 2000.
Supports batch processing of multiple animals from a single CSV file, with
flexible selection of animals and models. Produces per-animal parameter
tables, goodness-of-fit metrics including R-squared (R2), Root Mean Square
Error (RMSE), Akaike Information Criterion (AIC), Bayesian Information
Criterion (BIC), and a serial autocorrelation statistic, 15 diagnostic
figures, and combined cross-animal comparison outputs. References:
<doi:10.1085/jgp.5.4.441>, <doi:10.1038/216164a0>,
<doi:10.1016/0301-6226(87)90003-0>, <doi:10.4141/cjas87-067>,
<doi:10.3168/jds.S0022-0302(00)75136-8>.

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
