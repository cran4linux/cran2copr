%global __brp_check_rpaths %{nil}
%global packname  ensr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Elastic Net SearcheR

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 

%description
Elastic net regression models are controlled by two parameters, lambda, a
measure of shrinkage, and alpha, a metric defining the model's location on
the spectrum between ridge and lasso regression. glmnet provides tools for
selecting lambda via cross validation but no automated methods for
selection of alpha.  Elastic Net SearcheR automates the simultaneous
selection of both lambda and alpha. Developed, in part, with support by
NICHD R03 HD094912.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
