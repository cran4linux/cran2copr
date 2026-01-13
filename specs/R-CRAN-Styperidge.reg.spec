%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Styperidge.reg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          S-Type Ridge Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mctest 
BuildRequires:    R-CRAN-isdals 
BuildRequires:    R-CRAN-ridgregextra 
BuildRequires:    R-CRAN-Stype.est 
Requires:         R-stats 
Requires:         R-CRAN-mctest 
Requires:         R-CRAN-isdals 
Requires:         R-CRAN-ridgregextra 
Requires:         R-CRAN-Stype.est 

%description
Implements S-type ridge regression, a robust and multicollinearity-aware
linear regression estimator that combines S-type robust weighting (via the
'Stype.est' package) with ridge penalization; automatically selects the
ridge parameter using the 'ridgregextra' approach targeting a close to 1
variance inflation factor (VIF), and returns comprehensive outputs
(coefficients, fitted values, residuals, mean squared error (MSE), etc.)
with an easy x/y interface and optional user-supplied weights. See Sazak
and Mutlu (2021) <doi:10.1080/03610918.2021.1928196>, Karadag et al.
(2023) <https://CRAN.R-project.org/package=ridgregextra> and Sazak et al.
(2025) <https://CRAN.R-project.org/package=Stype.est>.

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
