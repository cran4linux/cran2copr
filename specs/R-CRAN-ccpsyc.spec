%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ccpsyc
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Cross-Cultural Psychology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-RcppAlgos 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-RcppAlgos 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Combines multiple functions that automate and simplify methods commonly
employed in cross-cultural psychology, providing a unified analysis
approach for measurement invariance testing, effect sizes for differential
item functioning, factor congruence and multi-group reliability. Methods
follow Fischer and Karl (2019) <doi:10.3389/fpsyg.2019.01507> and Gunn,
Grimm and Edwards (2020) <doi:10.1080/10705511.2019.1689507>.

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
