%global packname  ViSiElse
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          A Visual Tool for Behavior Analysis

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
Requires:         R-methods >= 3.2.0
Requires:         R-grid >= 3.2.0
Requires:         R-CRAN-chron >= 2.3.46
Requires:         R-CRAN-colorspace >= 1.2.6
Requires:         R-Matrix >= 1.2.0
Requires:         R-CRAN-stringr >= 1.0.0

%description
A graphical tool designed to visualize and to give an overview of
behavioral observations realized on individuals or groups. Visualization
of raw data during experimental observations of the realization of a
procedure. It graphically presents an overview of individuals and group
actions usually acquired from timestamps during video recorded sessions.
Options of the package allow adding graphical information as statistical
indicators (mean, standard deviation, quantile or statistical test) but
also for each action green or black zones providing visual information
about the accuracy of the realized actions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
