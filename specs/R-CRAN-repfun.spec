%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  repfun
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Create Tables, Listings and Figures using Functions Styled after SAS™ Macros

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xportr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-r2rtf 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xportr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-r2rtf 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 

%description
Mimic the style of traditional reporting macros for clinical trials. The
purpose is to generate tables, listings and figures that support clinical
research. This package is well suited for firms or individuals who wish to
incorporate R without changing their ways of working as it follows a
traditional clinical research workflow. Invoke functions (instead of
macros) to summarize data and produce formatted reports. This package
differs from others in that it includes tools (wrappers) for both
analyzing and reporting data.

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
