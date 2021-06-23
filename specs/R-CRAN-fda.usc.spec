%global __brp_check_rpaths %{nil}
%global packname  fda.usc
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Functional Data Analysis and Utilities for Statistical Computing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-splines 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-fda 
Requires:         R-splines 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-nlme 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-foreach 

%description
Routines for exploratory and descriptive analysis of functional data such
as depth measurements, atypical curves detection, regression models,
supervised classification, unsupervised classification and functional
analysis of variance.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/script
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
