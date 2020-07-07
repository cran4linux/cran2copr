%global packname  networkTomography
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}
Summary:          Tools for network tomography

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-limSolve >= 1.4
BuildRequires:    R-CRAN-KFAS >= 1.0
BuildRequires:    R-CRAN-igraph >= 0.5
BuildRequires:    R-CRAN-Rglpk >= 0.3
BuildRequires:    R-CRAN-coda >= 0.11.3
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-limSolve >= 1.4
Requires:         R-CRAN-KFAS >= 1.0
Requires:         R-CRAN-igraph >= 0.5
Requires:         R-CRAN-Rglpk >= 0.3
Requires:         R-CRAN-coda >= 0.11.3
Requires:         R-CRAN-plyr 

%description
networkTomography implements the methods developed and evaluated in
Blocker and Airoldi (2011) and Airoldi and Blocker (2012). These include
the authors' own dynamic multilevel model with calibration based upon a
Gaussian state-space model in addition to implementations of the methods
of Tebaldi & West (1998; Poisson-Gamma model with MCMC sampling), Zhang et
al. (2002; tomogravity), Cao et al. (2000; Gaussian model with
mean-variance relation), and Vardi (1996; method of moments). Data from
the 1router network of Cao et al. (2000), the Abilene network of Fang et
al. (2007), and the CMU network of Blocker and Airoldi (2011) are included
for testing and reproducibility.

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
