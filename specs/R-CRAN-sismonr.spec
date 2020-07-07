%global packname  sismonr
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}
Summary:          Simulation of in Silico Multi-Omic Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XRJulia >= 0.9.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XR 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-XRJulia >= 0.9.0
Requires:         R-parallel 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-tictoc 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XR 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-CRAN-scales 

%description
A tool for the simulation of gene expression profiles for in silico
regulatory networks. The package generates gene regulatory networks, which
include protein-coding and noncoding genes linked via different types of
regulation: regulation of transcription, translation, RNA or protein
decay, and post-translational modifications. The effect of genetic
mutations on the system behaviour is accounted for via the simulation of
genetically different in silico individuals. The ploidy of the system is
not restricted to the usual haploid or diploid situations, but is defined
by the user. A choice of stochastic simulation algorithms allow us to
simulate the expression profiles (RNA and if applicable protein abundance)
of the genes in the in silico system for the different in silico
individuals. A tutorial explaining how to use the package is available at
<https://oliviaab.github.io/sismonr/>. Manuscript in preparation; see also
Angelin-Bonnet O., Biggs P.J. and Vignes M. (2018)
<doi:10.1109/BIBM.2018.8621131>. Note that sismonr relies on Julia code
called internally by the functions. No knowledge of Julia is required in
order to use sismonr, but Julia must be installed on the computer
(instructions can be found in the tutorial, the GitHub page or the
vignette of the package).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/julia
%{rlibdir}/%{packname}/INDEX
