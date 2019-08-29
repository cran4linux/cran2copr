%global packname  BEACH
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Biometric Exploratory Analysis Creation House

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-WriteXLS >= 3.5.1
BuildRequires:    R-CRAN-devtools >= 1.9
BuildRequires:    R-CRAN-plyr >= 1.8.2
BuildRequires:    R-CRAN-xtable >= 1.7.4
BuildRequires:    R-CRAN-rJava >= 0.9.6
BuildRequires:    R-CRAN-sas7bdat >= 0.5
BuildRequires:    R-CRAN-rtf >= 0.4.11
BuildRequires:    R-CRAN-shiny >= 0.12.2
BuildRequires:    R-CRAN-haven >= 0.1.1
BuildRequires:    R-CRAN-DT >= 0.1
Requires:         R-CRAN-WriteXLS >= 3.5.1
Requires:         R-CRAN-devtools >= 1.9
Requires:         R-CRAN-plyr >= 1.8.2
Requires:         R-CRAN-xtable >= 1.7.4
Requires:         R-CRAN-rJava >= 0.9.6
Requires:         R-CRAN-sas7bdat >= 0.5
Requires:         R-CRAN-rtf >= 0.4.11
Requires:         R-CRAN-shiny >= 0.12.2
Requires:         R-CRAN-haven >= 0.1.1
Requires:         R-CRAN-DT >= 0.1

%description
A platform is provided for interactive analyses with a goal of totally
easy to develop, deploy, interact, and explore (TEDDIE). Using this
package, users can create customized analyses and make them available to
end users who can perform interactive analyses and save analyses to RTF or
HTML files. It allows developers to focus on R code for analysis, instead
of dealing with html or shiny code.

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
%doc %{rlibdir}/%{packname}/app
%{rlibdir}/%{packname}/INDEX
