%global packname  duawranglr
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}
Summary:          Securely Wrangle Dataset According to Data Usage Agreement

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 

%description
Create shareable data sets from raw data files that contain protected
elements. Relying on master crosswalk files that list restricted
variables, package functions warn users about possible violations of data
usage agreement and prevent writing protected elements.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
