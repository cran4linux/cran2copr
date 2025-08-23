%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lancor
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference via Lancaster Correlation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-boot 
Requires:         R-graphics 
Requires:         R-CRAN-sn 
Requires:         R-stats 

%description
Implementation of the methods described in Holzmann, Klar (2024) <doi:
10.1111/sjos.12733>. Lancaster correlation is a correlation coefficient
which equals the absolute value of the Pearson correlation for the
bivariate normal distribution, and is equal to or slightly less than the
maximum correlation coefficient for a variety of bivariate distributions.
Rank and moment-based estimators and corresponding confidence intervals
are implemented, as well as independence tests based on these statistics.

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
