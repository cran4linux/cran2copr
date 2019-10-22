%global packname  LLSR
%global packver   0.0.2.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2.19
Release:          1%{?dist}
Summary:          Data Analysis of Liquid-Liquid Systems using R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-XLConnect 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-svDialogs 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-XLConnect 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-svDialogs 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-crayon 

%description
Originally design to characterise Aqueous Two Phase Systems, LLSR provide
a simple way to analyse experimental data and obtain phase diagram
parameters, among other properties, systematically. The package will
include (every other update) new functions in order to comprise useful
tools in liquid-liquid extraction research.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
