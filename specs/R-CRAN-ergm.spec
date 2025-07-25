%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ergm
%global packver   4.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Exponential-Family Models for Networks

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-lpSolveAPI >= 5.5.2.0.17.14
BuildRequires:    R-CRAN-statnet.common >= 4.12.0
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-Rdpack >= 2.6.4
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-knitr >= 1.50
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-network >= 1.19.0
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-purrr >= 1.0.4
BuildRequires:    R-CRAN-robustbase >= 0.99.4.1
BuildRequires:    R-CRAN-coda >= 0.19.4.1
BuildRequires:    R-CRAN-rle >= 0.10.0
BuildRequires:    R-CRAN-trust >= 0.1.8
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-CRAN-lpSolveAPI >= 5.5.2.0.17.14
Requires:         R-CRAN-statnet.common >= 4.12.0
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-Rdpack >= 2.6.4
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-knitr >= 1.50
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-network >= 1.19.0
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-purrr >= 1.0.4
Requires:         R-CRAN-robustbase >= 0.99.4.1
Requires:         R-CRAN-coda >= 0.19.4.1
Requires:         R-CRAN-rle >= 0.10.0
Requires:         R-CRAN-trust >= 0.1.8
Requires:         R-parallel 
Requires:         R-methods 

%description
An integrated set of tools to analyze and simulate networks based on
exponential-family random graph models (ERGMs). 'ergm' is a part of the
Statnet suite of packages for network analysis. See Hunter, Handcock,
Butts, Goodreau, and Morris (2008) <doi:10.18637/jss.v024.i03> and
Krivitsky, Hunter, Morris, and Klumb (2023) <doi:10.18637/jss.v105.i06>.

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
