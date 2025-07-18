%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2rpt
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Templated Word and PowerPoint Reporting of 'nlmixr2' Fitting Results

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nlmixr2extra >= 2.0.7
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-nlmixr2est 
BuildRequires:    R-CRAN-onbrand 
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xpose 
BuildRequires:    R-CRAN-xpose.nlmixr2 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-nlmixr2extra >= 2.0.7
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-nlmixr2est 
Requires:         R-CRAN-onbrand 
Requires:         R-CRAN-rxode2 
Requires:         R-utils 
Requires:         R-CRAN-xpose 
Requires:         R-CRAN-xpose.nlmixr2 
Requires:         R-CRAN-yaml 

%description
This allows you to generate reporting workflows around 'nlmixr2' analyses
with outputs in Word and PowerPoint. You can specify figures, tables and
report structure in a user-definable 'YAML' file. Also you can use the
internal functions to access the figures and tables to allow their
including in other outputs (e.g. R Markdown).

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
