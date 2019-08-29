%global packname  MDplot
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Visualising Molecular Dynamics Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-gtools 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-gtools 

%description
Provides automatization for plot generation succeeding common molecular
dynamics analyses. This includes straightforward plots, such as RMSD
(Root-Mean-Square-Deviation) and RMSF (Root-Mean-Square-Fluctuation) but
also more sophisticated ones such as dihedral angle maps, hydrogen bonds,
cluster bar plots and DSSP (Definition of Secondary Structure of Proteins)
analysis. Currently able to load GROMOS, GROMACS and AMBER formats,
respectively.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bash
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
