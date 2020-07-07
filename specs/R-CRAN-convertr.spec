%global packname  convertr
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Convert Between Units

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-shiny >= 0.13.2
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-DT >= 0.1
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-DT >= 0.1

%description
Provides conversion functionality between a broad range of scientific,
historical, and industrial unit types.

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
%doc %{rlibdir}/%{packname}/media
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
