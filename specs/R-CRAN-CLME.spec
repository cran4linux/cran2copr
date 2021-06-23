%global __brp_check_rpaths %{nil}
%global packname  CLME
%global packver   2.0-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.12
Release:          2%{?dist}%{?buildtag}
Summary:          Constrained Inference for Linear Mixed Effects Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-isotone 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-prettyR 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-methods 
Requires:         R-CRAN-isotone 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-prettyR 
Requires:         R-stats 
Requires:         R-CRAN-openxlsx 
Requires:         R-graphics 

%description
Estimation and inference for linear models where some or all of the
fixed-effects coefficients are subject to order restrictions. This package
uses the robust residual bootstrap methodology for inference, and can
handle some structure in the residual variance matrix.

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
