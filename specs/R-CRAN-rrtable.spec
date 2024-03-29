%global __brp_check_rpaths %{nil}
%global packname  rrtable
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Research with a Table of R Codes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-flextable >= 0.4.4
BuildRequires:    R-CRAN-officer >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-moonBook >= 0.1.8
BuildRequires:    R-CRAN-ztable >= 0.1.8
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rvg 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-editData 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-flextable >= 0.4.4
Requires:         R-CRAN-officer >= 0.4.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-moonBook >= 0.1.8
Requires:         R-CRAN-ztable >= 0.1.8
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rvg 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-devEMF 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-editData 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-rlang 

%description
Makes documents containing plots and tables from a table of R codes. Can
make "HTML", "pdf('LaTex')", "docx('MS Word')" and "pptx('MS Powerpoint')"
documents with or without R code. In the package, modularized 'shiny' app
codes are provided. These modules are intended for reuse across
applications.

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
