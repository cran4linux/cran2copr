%global __brp_check_rpaths %{nil}
%global packname  dynsurv
%global packver   0.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Models for Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-BH >= 1.54.0.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-splines2 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Time-varying coefficient models for interval censored and right censored
survival data including 1) Bayesian Cox model with time-independent,
time-varying or dynamic coefficients for right censored and interval
censored data studied by Sinha et al. (1999)
<doi:10.1111/j.0006-341X.1999.00585.x> and Wang et al. (2013)
<doi:10.1007/s10985-013-9246-8>, 2) Spline based time-varying coefficient
Cox model for right censored data proposed by Perperoglou et al. (2006)
<doi:10.1016/j.cmpb.2005.11.006>, and 3) Transformation model with
time-varying coefficients for right censored data using estimating
equations proposed by Peng and Huang (2007) <doi:10.1093/biomet/asm058>.

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
