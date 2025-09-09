%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  texor
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Converting 'LaTeX' 'R Journal' Articles into 'RJ-web-articles'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-rjtools 
BuildRequires:    R-CRAN-rebib 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-desc 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-pdftools 
Requires:         R-tools 
Requires:         R-CRAN-tinytex 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-rjtools 
Requires:         R-CRAN-rebib 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-desc 

%description
Articles in the 'R Journal' were first authored in 'LaTeX', which performs
admirably for 'PDF' files but is less than ideal for modern online
interfaces. The 'texor' package does all the transitional chores and
conversions necessary to move to the online versions.

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
