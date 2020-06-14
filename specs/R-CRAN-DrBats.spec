%global packname  DrBats
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Data Representation: Bayesian Approach That's Sparse

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-sde 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-coda 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-sde 

%description
Feed longitudinal data into a Bayesian Latent Factor Model to obtain a
low-rank representation. Parameters are estimated using a Hamiltonian
Monte Carlo algorithm with STAN. See G. Weinrott, B. Fontez, N. Hilgert
and S. Holmes, "Bayesian Latent Factor Model for Functional Data
Analysis", Actes des JdS 2016.

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
