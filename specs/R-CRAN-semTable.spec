%global __brp_check_rpaths %{nil}
%global packname  semTable
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          2%{?dist}%{?buildtag}
Summary:          Structural Equation Modeling Tables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-kutils 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stationery 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-kutils 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stationery 

%description
For confirmatory factor analysis ('CFA') and structural equation models
('SEM') estimated with the 'lavaan' package, this package provides
functions to create model summary tables and model comparison tables for
hypothesis testing. Tables can be produced in 'LaTeX', 'HTML', or comma
separated variables ('CSV').

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
