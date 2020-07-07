%global packname  OptimaRegion
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Confidence Regions for Optima

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-DepthProc 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rdsdp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-stringr 
Requires:         R-boot 
Requires:         R-CRAN-DepthProc 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-rsm 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rdsdp 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-stringr 

%description
Computes confidence regions on the location of response surface optima.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
