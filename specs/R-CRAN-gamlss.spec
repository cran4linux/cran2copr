%global packname  gamlss
%global packver   5.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalised Additive Models for Location Scale and Shape

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-gamlss.data >= 5.0.0
BuildRequires:    R-CRAN-gamlss.dist >= 4.3.1
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-survival 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss.data >= 5.0.0
Requires:         R-CRAN-gamlss.dist >= 4.3.1
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-nlme 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-survival 
Requires:         R-methods 

%description
Functions for fitting the Generalized Additive Models for Location Scale
and Shape introduced by Rigby and Stasinopoulos (2005),
<doi:10.1111/j.1467-9876.2005.00510.x>. The models use a distributional
regression approach where all the parameters of the conditional
distribution of the response variable are modelled using explanatory
variables.

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
