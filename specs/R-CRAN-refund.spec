%global packname  refund
%global packver   0.1-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.17
Release:          1%{?dist}
Summary:          Regression with Functional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-mgcv >= 1.8.12
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-Matrix 
BuildRequires:    R-lattice 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbs 
BuildRequires:    R-methods 
Requires:         R-mgcv >= 1.8.12
Requires:         R-CRAN-fda 
Requires:         R-Matrix 
Requires:         R-lattice 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-magic 
Requires:         R-nlme 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-RLRsim 
Requires:         R-splines 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-pbs 
Requires:         R-methods 

%description
Methods for regression for functional data, including function-on-scalar,
scalar-on-function, and function-on-function regression. Some of the
functions are applicable to image data.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
