%global packname  midasr
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Data Sampling Regression

License:          GPL-2 | MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-methods 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-texreg 
Requires:         R-methods 

%description
Methods and tools for mixed frequency time series data analysis. Allows
estimation, model selection and forecasting for MIDAS regressions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
