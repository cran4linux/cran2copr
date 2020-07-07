%global packname  cofeatureR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Generate Cofeature Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-lazyeval >= 0.1.10
Requires:         R-CRAN-tibble 

%description
Generate cofeature (feature by sample) matrices. The package utilizes
ggplot2::geom_tile() to generate the matrix allowing for easy additions
from the base matrix.

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
