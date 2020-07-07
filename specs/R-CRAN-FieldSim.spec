%global packname  FieldSim
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          3%{?dist}
Summary:          Random Fields (and Bridges) Simulations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-methods 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-RColorBrewer 

%description
Tools for random fields and bridges simulations.

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
