%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R4GoodPersonalFinances
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Make Optimal Financial Decisions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-PrettyCols 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-PrettyCols 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-rlang 

%description
Make optimal decisions for your personal or household finances. Use tools
and methods that are selected carefully to align with academic consensus,
bridging the gap between theoretical knowledge and practical application.
They help you find your own personalized optimal discretionary spending or
optimal asset allocation, and prepare you for retirement or financial
independence. The optimal solution to this problems is extremely complex,
and we only have a single lifetime to get it right. Fortunately, we now
have the user-friendly tools implemented, that integrate life-cycle models
with single-period net-worth mean-variance optimization models. Those
tools can be used by anyone who wants to see what highly-personalized
optimal decisions can look like. For more details see: Idzorek T., Kaplan
P. (2024, ISBN:9781952927379), Haghani V., White J. (2023,
ISBN:9781119747918).

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
