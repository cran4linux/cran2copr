%global packname  iDynoR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          R Analysis package for iDynoMiCS Simulation Results

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-vegan 

%description
iDynoMiCS is a computer program, developed by an international team of
researchers, whose purpose is to model and simulate microbial communities
in an individual-based way. It is described in detail in the paper
"iDynoMiCS: next-generation individual-based modelling of biofilms" by
Lardon et al, published in Environmental Microbiology in 2011. The
simulation produces results in XML file format, describing the state of
each species in each timestep (agent_State), a summary of the species
statistics for a timepoint (agent_Sum), the state of each solute grid in
each timestep (env_State) and a summary of the solutes for a timestep
(env_Sum). This R package provides a means of reading this XML data into R
such that the simulation response can be statistically analysed. iDynoMiCS
is available from the website iDynoMiCS.org, where a full tutorial on
using both the simulation and this R package is provided.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
