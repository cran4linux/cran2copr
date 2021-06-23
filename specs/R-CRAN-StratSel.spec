%global __brp_check_rpaths %{nil}
%global packname  StratSel
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}%{?buildtag}
Summary:          Strategic Selection Estimator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-memisc 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-pbivnorm 
Requires:         R-MASS 
Requires:         R-CRAN-memisc 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-pbivnorm 

%description
Provides functions to estimate a strategic selection estimator. A
strategic selection estimator is an agent error model in which the two
random components are not assumed to be orthogonal. In addition this
package provides generic functions to print and plot objects of its class
as well as the necessary functions to create tables for LaTeX. There is
also a function to create dyadic data sets.

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
