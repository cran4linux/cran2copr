%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  targets
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Function-Oriented 'Make'-Like Declarative Pipelines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.4.3
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-withr >= 2.4.0
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-base64url >= 1.4
BuildRequires:    R-CRAN-knitr >= 1.34
BuildRequires:    R-CRAN-igraph >= 1.2.5
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.25
BuildRequires:    R-CRAN-vctrs >= 0.2.4
BuildRequires:    R-CRAN-codetools >= 0.2.16
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr >= 3.4.3
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-withr >= 2.4.0
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-base64url >= 1.4
Requires:         R-CRAN-knitr >= 1.34
Requires:         R-CRAN-igraph >= 1.2.5
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.25
Requires:         R-CRAN-vctrs >= 0.2.4
Requires:         R-CRAN-codetools >= 0.2.16
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Pipeline tools coordinate the pieces of computationally demanding analysis
projects. The 'targets' package is a 'Make'-like pipeline tool for
statistics and data science in R. The package skips costly runtime for
tasks that are already up to date, orchestrates the necessary computation
with implicit parallel computing, and abstracts files as R objects. If all
the current output matches the current upstream code and data, then the
whole pipeline is up to date, and the results are more trustworthy than
otherwise. The methodology in this package borrows from GNU 'Make' (2015,
ISBN:978-9881443519) and 'drake' (2018, <doi:10.21105/joss.00550>).

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
