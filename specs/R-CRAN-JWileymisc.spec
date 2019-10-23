%global packname  JWileymisc
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Miscellaneous Utilities and Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-VGAM >= 1.0.6
BuildRequires:    R-CRAN-lavaan >= 0.5.20
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-nlme 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-VGAM >= 1.0.6
Requires:         R-CRAN-lavaan >= 0.5.20
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-devtools 
Requires:         R-graphics 
Requires:         R-CRAN-ggthemes 
Requires:         R-mgcv 
Requires:         R-CRAN-mice 
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-quantreg 
Requires:         R-nlme 
Requires:         R-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 

%description
A collection of miscellaneous tools and functions, such as tools to
generate descriptive statistics tables, format output, visualize relations
among variables or check distributions.

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
%{rlibdir}/%{packname}/INDEX
