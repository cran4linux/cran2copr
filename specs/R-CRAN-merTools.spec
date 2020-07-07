%global packname  merTools
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          2%{?dist}
Summary:          Tools for Analyzing Mixed Effect Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1.11
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-blme 
BuildRequires:    R-CRAN-broom.mixed 
Requires:         R-CRAN-lme4 >= 1.1.11
Requires:         R-CRAN-arm 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-blme 
Requires:         R-CRAN-broom.mixed 

%description
Provides methods for extracting results from mixed-effect model objects
fit with the 'lme4' package. Allows construction of prediction intervals
efficiently from large scale linear and generalized linear mixed-effects
models.

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
