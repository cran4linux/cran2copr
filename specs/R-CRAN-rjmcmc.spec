%global packname  rjmcmc
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          3%{?dist}
Summary:          Reversible-Jump MCMC Using Post-Processing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-madness 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-madness 
Requires:         R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mvtnorm 

%description
Performs reversible-jump Markov chain Monte Carlo (Green, 1995)
<doi:10.2307/2337340>, specifically the restriction introduced by Barker &
Link (2013) <doi:10.1080/00031305.2013.791644>. By utilising a 'universal
parameter' space, RJMCMC is treated as a Gibbs sampling problem.
Previously-calculated posterior distributions are used to quickly estimate
posterior model probabilities. Jacobian matrices are found using automatic
differentiation. For a detailed description of the package, see Gelling,
Schofield & Barker (2019) <doi:10.1111/anzs.12263>.

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
