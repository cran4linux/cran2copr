%global packname  ZeligEI
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Zelig Ecological Inference Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Zelig >= 5.1.0
BuildRequires:    R-CRAN-eiPack 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ei 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-methods 
Requires:         R-CRAN-Zelig >= 5.1.0
Requires:         R-CRAN-eiPack 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ei 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-jsonlite 
Requires:         R-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-methods 

%description
Add-on package for Zelig 5. Enables the use of a variety of ecological
inference models.

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
%doc %{rlibdir}/%{packname}/JSON
%{rlibdir}/%{packname}/INDEX
