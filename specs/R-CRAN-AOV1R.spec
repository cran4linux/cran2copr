%global packname  AOV1R
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inference in the Balanced One-Way ANOVA Model with Random Factor

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-utils 
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lazyeval 
Requires:         R-utils 

%description
Provides functions to perform statistical inference in the balanced
one-way ANOVA model with a random factor: confidence intervals, prediction
interval, and Weerahandi generalized pivotal quantities. References:
Burdick & Graybill (1992, ISBN-13: 978-0824786441); Weerahandi (1995)
<doi:10.1007/978-1-4612-0825-9>; Lin & Liao (2008)
<doi:10.1016/j.jspi.2008.01.001>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
