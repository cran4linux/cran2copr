%global packname  JWileymisc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Miscellaneous Utilities and Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-VGAM >= 1.0.6
BuildRequires:    R-CRAN-lavaan >= 0.6.3
BuildRequires:    R-CRAN-extraoperators >= 0.1.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-VGAM >= 1.0.6
Requires:         R-CRAN-lavaan >= 0.6.3
Requires:         R-CRAN-extraoperators >= 0.1.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-emmeans 
Requires:         R-graphics 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-cowplot 
Requires:         R-mgcv 
Requires:         R-CRAN-mice 
Requires:         R-methods 
Requires:         R-CRAN-psych 
Requires:         R-grid 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-lme4 

%description
Miscellaneous tools and functions, including: generate descriptive
statistics tables, format output, visualize relations among variables or
check distributions, and generic functions for residual and model
diagnostics.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
