%global __brp_check_rpaths %{nil}
%global packname  shinyKGode
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          An Interactive Application for ODE Parameter Inference UsingGradient Matching

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.9
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-pracma >= 2.0.7
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-mvtnorm >= 1.0.6
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-pspline >= 1.0.18
BuildRequires:    R-CRAN-KGode >= 1.0.0
BuildRequires:    R-CRAN-shinyjs >= 0.9
Requires:         R-CRAN-XML >= 3.98.1.9
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-pracma >= 2.0.7
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-mvtnorm >= 1.0.6
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-pspline >= 1.0.18
Requires:         R-CRAN-KGode >= 1.0.0
Requires:         R-CRAN-shinyjs >= 0.9

%description
An interactive Shiny application to perform fast parameter inference on
dynamical systems (described by ordinary differential equations) using
gradient matching. Please see the project page for more details.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/application
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
