%global packname  MSEtool
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Management Strategy Evaluation Toolkit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-DLMtool >= 5.3.1
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-DLMtool >= 5.3.1
Requires:         R-MASS 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gplots 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rmarkdown 

%description
Simulation tools for management strategy evaluation are provided for the
'DLMtool' operating model to inform data-rich fisheries. 'MSEtool'
provides complementary assessment models of varying complexity with
standardized reporting, diagnostic tools for evaluating assessment models
within closed-loop simulation, and helper functions for building more
complex operating models and model-based management procedures.

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
