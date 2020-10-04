%global packname  RSPS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          RNA-Seq Power Simulation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-lattice 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-gridExtra 

%description
Provides functions for estimating power or sample size for RNA-Seq
studies. Empirical approach is used and the data is assumed to be count in
nature. The underlying distribution of data is assumed to be Poisson or
negative binomial. The package contains 6 function; 4 functions provide
estimates of sample size or power for Poisson and Negative Binomial
distribution; 2 functions provide plots of power for given sample size or
sample size for given power.

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
