%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimplyAgree
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible and Robust Agreement and Reliability Analyses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jmvcore 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jmvcore 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lifecycle 

%description
Reliability and agreement analyses often have limited software support.
Therefore, this package was created to make agreement and reliability
analyses easier for the average researcher. The functions within this
package include simple tests of agreement, agreement analysis for nested
and replicate data, and provide robust analyses of reliability. In
addition, this package contains a set of functions to help when planning
studies looking to assess measurement agreement.

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
