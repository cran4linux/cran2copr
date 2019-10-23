%global packname  openVA
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Automated Method for Verbal Autopsy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-InterVA4 >= 1.7.3
BuildRequires:    R-CRAN-InSilicoVA >= 1.1.3
BuildRequires:    R-CRAN-InterVA5 >= 1.0.1
BuildRequires:    R-CRAN-Tariff >= 1.0.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-InterVA4 >= 1.7.3
Requires:         R-CRAN-InSilicoVA >= 1.1.3
Requires:         R-CRAN-InterVA5 >= 1.0.1
Requires:         R-CRAN-Tariff >= 1.0.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 

%description
Implements multiple existing open-source algorithms for coding cause of
death from verbal autopsies. It also provides tools for data manipulation
tasks commonly used in Verbal Autopsy analysis and implements easy
graphical visualization of individual and population level statistics.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
