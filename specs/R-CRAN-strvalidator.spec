%global packname  strvalidator
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}
Summary:          Process Control and Internal Validation of Forensic STR Kits

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-gWidgets2tcltk 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-gWidgets2tcltk 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 

%description
An open source platform for validation and process control. Tools to
analyze data from internal validation of forensic short tandem repeat
(STR) kits are provided. The tools are developed to provide the necessary
data to conform with guidelines for internal validation issued by the
European Network of Forensic Science Institutes (ENFSI) DNA Working Group,
and the Scientific Working Group on DNA Analysis Methods (SWGDAM). A
front-end graphical user interface is provided. More information about
each function can be found in the respective help documentation.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
