%global packname  CUFF
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}
Summary:          Charles's Utility Function using Formula

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-nlme 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-lmerTest 
Requires:         R-nlme 

%description
Utility functions that provides wrapper to descriptive base functions like
cor, mean and table.  It makes use of the formula interface to pass
variables to functions.  It also provides operators to concatenate (%+%),
to repeat (%n%) and manage character vectors for nice display.

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
%{rlibdir}/%{packname}/INDEX
