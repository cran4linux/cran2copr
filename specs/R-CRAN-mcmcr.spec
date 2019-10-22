%global packname  mcmcr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Manipulate MCMC Samples

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-err 
BuildRequires:    R-CRAN-checkr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-err 
Requires:         R-CRAN-checkr 
Requires:         R-CRAN-coda 
Requires:         R-utils 
Requires:         R-stats 

%description
Functions and classes to store, manipulate and summarise Monte Carlo
Markov Chain (MCMC) samples. For more information see Brooks et al. (2011)
<isbn:978-1-4200-7941-8>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/JOSS
%{rlibdir}/%{packname}/INDEX
