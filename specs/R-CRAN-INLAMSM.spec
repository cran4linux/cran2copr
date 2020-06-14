%global packname  INLAMSM
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          2%{?dist}
Summary:          Multivariate Spatial Models with 'INLA'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-Matrix 
Requires:         R-CRAN-MCMCpack 

%description
Implementation of several multivariate areal latent effects for 'INLA'
using the 'rgeneric' latent effect (Palmí-Perales et al., 2019,
<arXiv:1909.10804>). The 'INLA' package can be downloaded from
<http://www.r-inla.org>. In particular, the package includes latent
effects ready to use for several multivariate spatial models: intrinsic
CAR, proper CAR and the M-model (Botella-Rocamora et al., 2015,
<doi:10.1002/sim.6423>).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
