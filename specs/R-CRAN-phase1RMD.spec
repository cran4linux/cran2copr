%global packname  phase1RMD
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          2%{?dist}
Summary:          Repeated Measurement Design for Phase I Clinical Trial

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-arrayhelpers 
Requires:         R-CRAN-coda 
Requires:         R-boot 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-arrayhelpers 

%description
Implements our Bayesian phase I repeated measurement design that accounts
for multidimensional toxicity endpoints from multiple treatment cycles.
The package also provides a novel design to account for both
multidimensional toxicity endpoints and early-stage efficacy endpoints in
the phase I design. For both designs, functions are provided to recommend
the next dosage selection based on the data collected in the available
patient cohorts and to simulate trial characteristics given design
parameters. Yin, Jun, et al. (2017) <doi:10.1002/sim.7134>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
