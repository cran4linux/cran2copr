%global packname  xgxr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Graphics for Pharmacometrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-png 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Supports a structured approach for exploring PKPD data
<https://opensource.nibr.com/xgx/>. It also contains helper functions for
enabling the modeler to follow best R practices (by appending the program
name, figure name location, and draft status to each plot). In addition,
it enables the modeler to follow best graphical practices (by providing a
theme that reduces chart ink, and by providing time-scale, log-scale, and
reverse-log-transform-scale functions for more readable axes). Finally, it
provides some data checking and summarizing functions for rapidly
exploring pharmacokinetics and pharmacodynamics (PKPD) datasets.

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
