%global packname  CARrampsOcl
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Reparameterized and marginalized posterior sampling forconditional autoregressive models, OpenCL implementation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    pocl-devel
Requires:         pocl
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-OpenCL 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-OpenCL 
Requires:         R-CRAN-fields 

%description
This package fits Bayesian conditional autoregressive models for spatial
and spatiotemporal data on a lattice.  It uses OpenCL kernels running on
GPUs to perform rejection sampling to obtain independent samples from the
joint posterior distribution of model parameters.

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
%{rlibdir}/%{packname}/libs
