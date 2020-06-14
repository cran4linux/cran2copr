%global packname  ViSiElse
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          2%{?dist}
Summary:          A Visual Tool for Behavior Analysis over Time

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.2.0
BuildRequires:    R-grid >= 3.2.0
BuildRequires:    R-CRAN-chron >= 2.3.46
BuildRequires:    R-CRAN-colorspace >= 1.2.6
BuildRequires:    R-Matrix >= 1.2.0
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-methods >= 3.2.0
Requires:         R-grid >= 3.2.0
Requires:         R-CRAN-chron >= 2.3.46
Requires:         R-CRAN-colorspace >= 1.2.6
Requires:         R-Matrix >= 1.2.0
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
A graphical R package designed to visualize behavioral observations over
time. Based on raw time data extracted from video recorded sessions of
experimental observations, ViSiElse grants a global overview of a process
by combining the visualization of multiple actions timestamps for all
participants in a single graph. Individuals and/or group behavior can
easily be assessed. Supplementary features allow users to further inspect
their data by adding summary statistics (mean, standard deviation,
quantile or statistical test) and/or time constraints to assess the
accuracy of the realized actions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
