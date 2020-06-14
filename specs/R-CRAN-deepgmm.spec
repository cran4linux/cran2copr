%global packname  deepgmm
%global packver   0.1.59
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.59
Release:          2%{?dist}
Summary:          Deep Gaussian Mixture Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor 

%description
Deep Gaussian mixture models as proposed by Viroli and McLachlan (2019)
<doi:10.1007/s11222-017-9793-z> provide a generalization of classical
Gaussian mixtures to multiple layers. Each layer contains a set of latent
variables that follow a mixture of Gaussian distributions. To avoid
overparameterized solutions, dimension reduction is applied at each layer
by way of factor models.

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
