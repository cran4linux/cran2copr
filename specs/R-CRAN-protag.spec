%global packname  protag
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Search Tagged Peptides & Draw Highlighted Mass Spectra

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 

%description
In a typical protein labelling procedure, proteins are chemically tagged
with a functional group, usually at specific sites, then digested into
peptides, which are then analyzed using matrix-assisted laser desorption
ionization - time of flight mass spectrometry (MALDI-TOF MS) to generate
peptide fingerprint. Relative to the control, peptides that are heavier by
the mass of the labelling group are informative for sequence
determination. Searching for peptides with such mass shifts, however, can
be difficult. This package, designed to tackle this inconvenience, takes
as input the mass list of two or multiple MALDI-TOF MS mass lists, and
makes pairwise comparisons between the labeled groups vs. control, and
restores centroid mass spectra with highlighted peaks of interest for
easier visual examination. Particularly, peaks differentiated by the mass
of the labelling group are defined as a “pair”, those with equal masses as
a “match”, and all the other peaks as a “mismatch”.For more bioanalytical
background information, refer to following publications: Jingjing Deng
(2015) <doi:10.1007/978-1-4939-2550-6_19>; Elizabeth Chang (2016)
<doi:10.7171/jbt.16-2702-002>.

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
