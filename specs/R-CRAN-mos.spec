%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mos
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Moment Computation for Order Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-hypergeo2 
Requires:         R-stats 
Requires:         R-CRAN-hypergeo2 

%description
Provides a comprehensive set of tools for working with order statistics,
including functions for simulating order statistics, censored samples
(Type I and Type II), and record values from various continuous
distributions. Additionally, it offers functions to compute moments (mean,
variance, skewness, kurtosis) of order statistics for several continuous
distributions. These tools assist researchers and statisticians in
understanding and analyzing the properties of order statistics and related
data. The methods and algorithms implemented in this package are based on
several published works, including Ahsanullah et al (2013,
ISBN:9789491216831), Arnold and Balakrishnan (2012, ISBN:1461236444),
Harter and Balakrishnan (1996, ISBN:9780849394522), Balakrishnan and
Sandhu (1995) <doi:10.1080/00031305.1995.10476150>, Genç (2012)
<doi:10.1007/s00362-010-0320-y>, Makouei et al (2021)
<doi:10.1016/j.cam.2021.113386> and Nagaraja (2013)
<doi:10.1016/j.spl.2013.06.028>.

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
