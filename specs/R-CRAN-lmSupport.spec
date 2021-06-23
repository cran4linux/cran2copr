%global __brp_check_rpaths %{nil}
%global packname  lmSupport
%global packver   2.9.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.13
Release:          2%{?dist}%{?buildtag}
Summary:          Support for Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gvlma 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gvlma 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-pbkrtest 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-pwr 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools and a consistent interface to support analyses using
General, Generalized, and Multi-level Linear Models.

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
