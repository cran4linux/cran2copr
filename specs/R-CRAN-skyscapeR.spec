%global packname  skyscapeR
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Skyscape Archaeology Data Reduction, Visualization and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-astrolibR 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-oce 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MESS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-astrolibR 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-png 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-oce 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MESS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rootSolve 

%description
A toolset for data reduction, visualization and analysis in skyscape
archaeology, archaeoastronomy and cultural astronomy.

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
%{rlibdir}/%{packname}/INDEX
