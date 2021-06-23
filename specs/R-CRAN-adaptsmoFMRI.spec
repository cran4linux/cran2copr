%global __brp_check_rpaths %{nil}
%global packname  adaptsmoFMRI
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Adaptive Smoothing of FMRI Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-parallel 
Requires:         R-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-spatstat 
Requires:         R-parallel 

%description
This package contains R functions for estimating the blood oxygenation
level dependent (BOLD) effect by using functional Magnetic Resonance
Imaging (fMRI) data, based on adaptive Gauss Markov random fields, for
real as well as simulated data. The implemented simulations make use of
efficient Markov Chain Monte Carlo methods.

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
