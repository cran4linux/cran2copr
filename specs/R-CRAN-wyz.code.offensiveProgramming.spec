%global __brp_check_rpaths %{nil}
%global packname  wyz.code.offensiveProgramming
%global packver   1.1.23
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.23
Release:          1%{?dist}%{?buildtag}
Summary:          Wizardry Code Offensive Programming

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 

%description
Allows to turn standard R code into offensive programming code. Provides
code instrumentation to ease this change and tools to assist and
accelerate code production and tuning while using offensive programming
code technics. Should improve code robustness and quality. Function calls
can be easily verified on-demand or in batch mode to assess parameter
types and length conformities. Should improve coders productivity as
offensive programming reduces the code size due to reduced number of
controls all along the call chain. Should speed up processing as many
checks will be reduced to one single check.

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
