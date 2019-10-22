%global packname  MBmca
%global packver   0.0.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3.5
Release:          1%{?dist}
Summary:          Nucleic Acid Melting Curve Analysis on Microbead Surfaces with R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase >= 0.9
BuildRequires:    R-CRAN-chipPCR >= 0.0.7
Requires:         R-CRAN-robustbase >= 0.9
Requires:         R-CRAN-chipPCR >= 0.0.7

%description
The MBmca package provides data sets and lightweight utilities for nucleic
acid melting curve analysis and presentation on microbead surfaces but
also for reactions in solution (e.g., qPCR).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/MBmca_logo.png
%{rlibdir}/%{packname}/INDEX
