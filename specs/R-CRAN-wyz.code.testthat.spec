%global __brp_check_rpaths %{nil}
%global packname  wyz.code.testthat
%global packver   1.1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.20
Release:          1%{?dist}%{?buildtag}
Summary:          Wizardry Code Offensive Programming Test Generation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-wyz.code.offensiveProgramming >= 1.1.22
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-wyz.code.offensiveProgramming >= 1.1.22
Requires:         R-methods 
Requires:         R-CRAN-tidyr 

%description
Allows to generate automatically 'testthat' code files from offensive
programming test cases. Generated test files are complete and ready to
run. Using 'wyz.code.testthat' you will earn a lot of time, reduce the
number of errors in test case production, be able to test immediately
generated files without any need to view or modify them, and enter a zero
time latency between code implementation and industrial testing. As with
'testthat', you may complete provided test cases according to your needs
to push testing further, but this need is nearly void when using
'wyz.code.offensiveProgramming'.

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
