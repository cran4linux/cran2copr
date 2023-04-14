%global __brp_check_rpaths %{nil}
%global packname  DOBAD
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Discretely Observed LinearBirth-and-Death(-and-Immigration) Markov Chains

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-Matrix 

%description
Provides Frequentist (EM) and Bayesian (MCMC) Methods for Inference of
Birth-Death-Immigration Markov Chains.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
