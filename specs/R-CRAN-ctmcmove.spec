%global packname  ctmcmove
%global packver   1.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.9
Release:          3%{?dist}
Summary:          Modeling Animal Movement with Continuous-Time Discrete-SpaceMarkov Chains

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-Matrix 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-sp 

%description
Software to facilitates taking movement data in xyt format and pairing it
with raster covariates within a continuous time Markov chain (CTMC)
framework.  As described in Hanks et al. (2015) <DOI:10.1214/14-AOAS803> ,
this allows flexible modeling of movement in response to covariates (or
covariate gradients) with model fitting possible within a Poisson GLM
framework.

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
