%global packname  canprot
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Chemical Composition of Differential Protein Expression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CHNOSZ >= 1.3.0
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-CHNOSZ >= 1.3.0
Requires:         R-CRAN-xtable 

%description
Datasets are collected here for differentially (up- and down-) expressed
proteins identified in proteomic studies of cancer and in cell culture
experiments. Tables of amino acid compositions of proteins are used for
calculations of chemical composition, projected into selected basis
species. Plotting functions are used to visualize the compositional
differences and thermodynamic potentials for proteomic transformations.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
