%global packname  kim
%global packver   0.2.133
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.133
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Behavioral Science Researchers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-interactions 
BuildRequires:    R-CRAN-lemon 
BuildRequires:    R-CRAN-lm.beta 
BuildRequires:    R-CRAN-mediation 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-paran 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-WRS2 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-interactions 
Requires:         R-CRAN-lemon 
Requires:         R-CRAN-lm.beta 
Requires:         R-CRAN-mediation 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-paran 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-WRS2 

%description
Miscellaneous functions to simplify and expedite analyses of experimental
data. Examples include a function that plots sample means of groups in a
factorial experimental design, a function that conducts robust regressions
with bootstrapped samples, and a function that conducts robust two-way
analysis of variance.

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
