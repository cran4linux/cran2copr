%global packname  yotover
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Advanced Guide to Trade Policy Analysis

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-multiwayvcov 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-munsell 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-multiwayvcov 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-munsell 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-rstudioapi 

%description
On-disk embedded database with SQL versions of the original datasets from
Yotov, et al (2016, ISBN: 978-92-870-4367-2) and functions to report
regressions with clustered robust standard errors.

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
