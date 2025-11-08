%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EstemPMM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Polynomial Maximization Method for Non-Gaussian Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Implements the Polynomial Maximization Method ('PMM') for parameter
estimation in linear and time series models when error distributions
deviate from normality. The 'PMM2' variant achieves lower variance
parameter estimates compared to ordinary least squares ('OLS') when errors
exhibit significant skewness. Includes methods for linear regression,
'AR'/'MA'/'ARMA'/'ARIMA' models, and bootstrap inference. Methodology
described in Zabolotnii, Warsza, and Tkachenko (2018)
<doi:10.1007/978-3-319-77179-3_75>, Zabolotnii, Tkachenko, and Warsza
(2022) <doi:10.1007/978-3-031-03502-9_37>, and Zabolotnii, Tkachenko, and
Warsza (2023) <doi:10.1007/978-3-031-25844-2_21>.

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
