%global __brp_check_rpaths %{nil}
%global packname  ifaTools
%global packver   0.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Item Factor Analysis with 'OpenMx'

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx >= 2.3.1
BuildRequires:    R-CRAN-rpf >= 0.48
BuildRequires:    R-CRAN-shiny >= 0.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
Requires:         R-CRAN-OpenMx >= 2.3.1
Requires:         R-CRAN-rpf >= 0.48
Requires:         R-CRAN-shiny >= 0.10
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 

%description
Tools, tutorials, and demos of Item Factor Analysis using 'OpenMx'. This
software is described in Pritikin & Falk (2020)
<doi:10.1177/0146621620929431>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
