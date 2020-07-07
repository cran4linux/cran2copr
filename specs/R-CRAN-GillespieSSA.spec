%global packname  GillespieSSA
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}
Summary:          Gillespie's Stochastic Simulation Algorithm (SSA)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a simple to use, intuitive, and extensible interface to several
stochastic simulation algorithms for generating simulated trajectories of
finite population continuous-time model. Currently it implements
Gillespie's exact stochastic simulation algorithm (Direct method) and
several approximate methods (Explicit tau-leap, Binomial tau-leap, and
Optimized tau-leap). The package also contains a library of template
models that can be run as demo models and can easily be customized and
extended. Currently the following models are included,
'Decaying-Dimerization' reaction set, linear chain system, logistic growth
model, 'Lotka' predator-prey model, Rosenzweig-MacArthur predator-prey
model, 'Kermack-McKendrick' SIR model, and a 'metapopulation' SIRS model.
Pineda-Krch et al. (2008) <doi:10.18637/jss.v025.i12>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
