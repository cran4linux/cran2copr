%global __brp_check_rpaths %{nil}
%global packname  frequency
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Frequency Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-utils 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-utils 

%description
Generate 'SPSS'/'SAS' styled frequency tables. Frequency tables are
generated with variable and value label attributes where applicable with
optional html output to quickly examine datasets.

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
