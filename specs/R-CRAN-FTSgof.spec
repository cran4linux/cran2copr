%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FTSgof
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          White Noise and Goodness-of-Fit Tests for Functional Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-sde 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-MASS 

%description
It offers comprehensive tools for the analysis of functional time series
data, focusing on white noise hypothesis testing and goodness-of-fit
evaluations, alongside functions for simulating data and advanced
visualization techniques, such as 3D rainbow plots. These methods are
described in Kokoszka, Rice, and Shang (2017)
<doi:10.1016/j.jmva.2017.08.004>, Yeh, Rice, and Dubin (2023)
<doi:10.1214/23-EJS2112>, Kim, Kokoszka, and Rice (2023)
<doi:10.1214/23-ss143>, and Rice, Wirjanto, and Zhao (2020)
<doi:10.1111/jtsa.12532>.

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
