%global packname  ndtv
%global packver   0.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.0
Release:          3%{?dist}
Summary:          Network Dynamic Temporal Visualizations

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-animation >= 2.4
BuildRequires:    R-CRAN-network >= 1.13
BuildRequires:    R-CRAN-networkDynamic >= 0.9
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-base64 
Requires:         R-CRAN-animation >= 2.4
Requires:         R-CRAN-network >= 1.13
Requires:         R-CRAN-networkDynamic >= 0.9
Requires:         R-CRAN-sna 
Requires:         R-MASS 
Requires:         R-CRAN-statnet.common 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-base64 

%description
Renders dynamic network data from 'networkDynamic' objects as movies,
interactive animations, or other representations of changing relational
structures and attributes.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/javascript
%{rlibdir}/%{packname}/INDEX
