%global packname  xpose4
%global packver   4.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.1
Release:          1%{?dist}
Summary:          Tools for Nonlinear Mixed-Effect Model Building and Diagnostics

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-splines 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-readr 
Requires:         R-lattice 
Requires:         R-CRAN-Hmisc 
Requires:         R-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-gam 
Requires:         R-splines 
Requires:         R-grid 
Requires:         R-CRAN-readr 

%description
A collection of functions to be used as a model building aid for nonlinear
mixed-effects (population) analysis using NONMEM. It facilitates data set
checkout, exploration and visualization, model diagnostics, candidate
covariate identification and model comparison.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/xpose.ini
%{rlibdir}/%{packname}/INDEX
