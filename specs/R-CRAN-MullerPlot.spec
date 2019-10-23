%global packname  MullerPlot
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Generates Muller Plot from Population/Abundance/FrequencyDynamics Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-graphics 

%description
Generates Muller plot from parental/genealogy/phylogeny information and
population/abundance/frequency dynamics data. Muller plots are plots which
combine information about succession of different OTUs (genotypes,
phenotypes, species, ...) and information about dynamics of their
abundances (populations or frequencies) over time. They are powerful and
fascinating tools to visualize evolutionary dynamics. They may be employed
also in study of diversity and its dynamics, i.e. how diversity emerges
and how changes over time. They are called Muller plots in honor of
Hermann Joseph Muller which used them to explain his idea of Muller's
ratchet (Muller, 1932, American Naturalist). A big difference between
Muller plots and normal box plots of abundances is that a Muller plot
depicts not only the relative abundances but also succession of OTUs based
on their genealogy/phylogeny/parental relation. In a Muller plot,
horizontal axis is time/generations and vertical axis represents relative
abundances of OTUs at the corresponding times/generations. Different OTUs
are usually shown with polygons with different colors and each OTU
originates somewhere in the middle of its parent area in order to
illustrate their succession in evolutionary process. To generate a Muller
plot one needs the genealogy/phylogeny/parental relation of OTUs and their
abundances over time. MullerPlot package has the tools to generate Muller
plots which clearly depict the origin of successors of OTUs.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
