%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inequality
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inequality Measurement, Decomposition, and Poverty Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Tools for measuring income and wealth inequality. Computes the Gini
coefficient with bootstrap or asymptotic confidence intervals following
Davidson (2009) <doi:10.1016/j.jeconom.2008.09.011>, the extended S-Gini
family, Theil T and L indices (generalised entropy family), the Atkinson
index, the Kolm absolute inequality index, Palma ratio, Hoover index,
percentile ratios, and Lorenz curves. Supports between-within group
decomposition following Bourguignon (1979) <doi:10.2307/1914138>, income
share tabulation, concentration indices for health inequality with
Erreygers (2009) correction, Kakwani tax progressivity and
Reynolds-Smolensky redistribution indices, Foster-Greer-Thorbecke poverty
measures including the Sen index, growth incidence curves following
Ravallion and Chen (2003) <doi:10.1016/S0165-1765(02)00205-7>, and Wolfson
polarisation. All functions accept optional survey weights and work with
data from any source.

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
