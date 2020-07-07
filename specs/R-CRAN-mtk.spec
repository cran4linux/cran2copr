%global packname  mtk
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Mexico ToolKit library (MTK)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-rgl 
Requires:         R-base 
Requires:         R-CRAN-stringr 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-rgl 

%description
MTK (Mexico ToolKit) is a generic platform for the sensitivity and
uncertainty analysis of complex models. It provides functions and
facilities for experimental design, model simulation, sensitivity and
uncertainty analysis, methods integration and data reporting, etc.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/manual
%{rlibdir}/%{packname}/INDEX
