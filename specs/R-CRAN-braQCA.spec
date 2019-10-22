%global packname  braQCA
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}
Summary:          Bootstrapped Robustness Assessment for Qualitative ComparativeAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-QCA 
BuildRequires:    R-CRAN-bootstrap 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-QCA 
Requires:         R-CRAN-bootstrap 

%description
Test the robustness of a user's Qualitative Comparative Analysis solutions
to randomness, using the bootstrapped assessment: baQCA(). This package
also includes a function that provides recommendations for improving
solutions to reach typical significance levels: brQCA(). After applying
recommendations from brQCA(), QCAdiff() shows which cases are excluded
from the final result.

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
%{rlibdir}/%{packname}/INDEX
