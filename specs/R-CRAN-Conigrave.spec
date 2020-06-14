%global packname  Conigrave
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          2%{?dist}
Summary:          Flexible Tools for Multiple Imputation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-miceadds >= 3.2.48
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-mitools >= 2.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-ppcor >= 1.1
BuildRequires:    R-CRAN-stringdist >= 0.9.5.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-miceadds >= 3.2.48
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-mitools >= 2.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-ppcor >= 1.1
Requires:         R-CRAN-stringdist >= 0.9.5.1
Requires:         R-CRAN-dplyr >= 0.8.0.1

%description
Provides a set of tools that can be used across 'data.frame' and
'imputationList' objects.

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
%{rlibdir}/%{packname}/INDEX
