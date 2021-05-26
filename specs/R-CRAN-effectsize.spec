%global packname  effectsize
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Indices of Effect Size and Standardized Parameters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-bayestestR >= 0.9.0
BuildRequires:    R-CRAN-insight >= 0.14.0
BuildRequires:    R-CRAN-parameters >= 0.13.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-bayestestR >= 0.9.0
Requires:         R-CRAN-insight >= 0.14.0
Requires:         R-CRAN-parameters >= 0.13.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provide utilities to work with indices of effect size and standardized
parameters for a wide variety of models (see list of supported models in
insight; Lüdecke, Waggoner & Makowski (2019) <doi:10.21105/joss.01412>),
allowing computation of and conversion between indices such as Cohen's d,
r, odds, etc.

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
