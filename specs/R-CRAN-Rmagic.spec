%global __brp_check_rpaths %{nil}
%global packname  Rmagic
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          MAGIC - Markov Affinity-Based Graph Imputation of Cells

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.4
BuildRequires:    R-Matrix >= 1.2.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-reticulate >= 1.4
Requires:         R-Matrix >= 1.2.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
MAGIC (Markov affinity-based graph imputation of cells) is a method for
addressing technical noise in single-cell data, including under-sampling
of mRNA molecules, often termed "dropout" which can severely obscure
important gene-gene relationships. MAGIC shares information across similar
cells, via data diffusion, to denoise the cell count matrix and fill in
missing transcripts. Read more: van Dijk et al. (2018)
<DOI:10.1016/j.cell.2018.05.061>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
