%global packname  spartan
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}
Summary:          Simulation Parameter Analysis R Toolkit ApplicatioN: 'spartan'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-mco 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-mlegp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-mco 

%description
Computer simulations are becoming a popular technique to use in attempts
to further our understanding of complex systems. 'spartan', first
described in our 2013 publication in PLoS Computational Biology, provided
code for four techniques described in available literature which aid the
analysis of simulation results, at both single and multiple timepoints in
the simulation run. The first technique addresses aleatory uncertainty in
the system caused through inherent stochasticity, and determines the
number of replicate runs necessary to generate a representative result.
The second examines how robust a simulation is to parameter perturbation,
through the use of a one-at-a-time parameter analysis technique. Thirdly,
a latin hypercube based sensitivity analysis technique is included which
can elucidate non-linear effects between parameters and indicate
implications of epistemic uncertainty with reference to the system being
modelled. Finally, a further sensitivity analysis technique, the extended
Fourier Amplitude Sampling Test (eFAST) has been included to partition the
variance in simulation results between input parameters, to determine the
parameters which have a significant effect on simulation behaviour.
Version 1.3 added support for Netlogo simulations, aiding simulation
developers who use Netlogo to build their simulations perform the same
analyses. Version 2.0 added the ability to read all simulations in from a
single CSV file in addition to the prescribed folder structure in previous
versions. Version 3.0 offers significant additional functionality that
permits the creation of emulations of simulation results, derived using
the same sampling techniques in the global sensitivity analysis
techniques, and the generation of combinations of these machine learning
algorithms to one create one predictive tool, more commonly known as an
ensemble model. Version 3.0 also improved the standard of the graphs
produced in the original sensitivity analysis techniques, and introduced a
polar plot to examine parameter sensitivity.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
