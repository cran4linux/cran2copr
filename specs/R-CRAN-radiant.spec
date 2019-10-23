%global packname  radiant
%global packver   0.9.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9.1
Release:          1%{?dist}
Summary:          Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-radiant.multivariate >= 0.9.9.1
BuildRequires:    R-CRAN-radiant.data >= 0.9.9
BuildRequires:    R-CRAN-radiant.design >= 0.9.9
BuildRequires:    R-CRAN-radiant.basics >= 0.9.9
BuildRequires:    R-CRAN-radiant.model >= 0.9.9
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-radiant.multivariate >= 0.9.9.1
Requires:         R-CRAN-radiant.data >= 0.9.9
Requires:         R-CRAN-radiant.design >= 0.9.9
Requires:         R-CRAN-radiant.basics >= 0.9.9
Requires:         R-CRAN-radiant.model >= 0.9.9

%description
A platform-independent browser-based interface for business analytics in
R, based on the shiny package. The application combines the functionality
of radiant.data, radiant.design, radiant.basics, radiant.model, and
radiant.multivariate.

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
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
