%global packname  stocc
%global packver   1.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.30
Release:          3%{?dist}
Summary:          Fit a Spatial Occupancy Model via Gibbs Sampling

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-rARPACK 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-coda 
Requires:         R-Matrix 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-rARPACK 

%description
Fit a spatial-temporal occupancy models using a probit formulation instead
of a traditional logit model.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
