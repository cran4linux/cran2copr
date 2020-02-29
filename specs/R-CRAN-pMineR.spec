%global debug_package %{nil}
%global packname  pMineR
%global packver   0.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.31
Release:          1%{?dist}
Summary:          Processes Mining in Medicine

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.3
BuildRequires:    R-cluster >= 2.0.4
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-DiagrammeR >= 0.8.2
Requires:         R-CRAN-XML >= 3.98.1.3
Requires:         R-cluster >= 2.0.4
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-DiagrammeR >= 0.8.2

%description
Allows to build and train simple Process Mining (PM) models. The aim is to
support PM specifically for the clinical domain from both administrative
and clinical data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
