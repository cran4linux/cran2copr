%global packname  MobileTrigger
%global packver   0.0.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.31
Release:          2%{?dist}
Summary:          Run Reports, Models, and Scripts from a Mobile Device

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-mailR 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-mailR 

%description
A framework for interacting with R modules such as Reports, Models, and
Scripts from a mobile device. The framework allows you to list available
modules and select a module of interest using a basic e-mail interface.
After selecting a specific module, you can either run it as is or provide
input via the e-mail interface. After parsing your request, R will send
the results back to your mobile device.

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
