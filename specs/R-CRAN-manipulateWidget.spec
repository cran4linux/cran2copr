%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manipulateWidget
%global packver   0.11.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.2
Release:          1%{?dist}%{?buildtag}
Summary:          Add Even More Interactivity to Interactive Charts

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-CRAN-base64enc 
Requires:         R-grDevices 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-shinyjs 

%description
Like package 'manipulate' does for static graphics, this package helps to
easily add controls like sliders, pickers, checkboxes, etc. that can be
used to modify the input data or the parameters of an interactive chart
created with package 'htmlwidgets'.

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
