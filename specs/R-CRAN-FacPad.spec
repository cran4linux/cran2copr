%global packname  FacPad
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          2%{?dist}
Summary:          Bayesian Sparse Factor Analysis model for the inference ofpathways responsive to drug treatment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.1
Requires:         R-core >= 2.12.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Rlab 
BuildRequires:    R-MASS 
Requires:         R-CRAN-Rlab 
Requires:         R-MASS 

%description
This method tries to explain the gene-wise treatment response ratios in
terms of the latent pathways. It uses bayesian sparse factor modeling to
infer the loadings (weights) of each pathway on its associated probesets
as well as the latent factor activity levels for each treatment.

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
%{rlibdir}/%{packname}/INDEX
