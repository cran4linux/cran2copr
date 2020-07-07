%global packname  motifcluster
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Motif-Based Spectral Clustering of Weighted Directed Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.2.5
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-LICORS >= 0.2.0
BuildRequires:    R-CRAN-RSpectra >= 0.16.0
Requires:         R-CRAN-igraph >= 1.2.5
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-LICORS >= 0.2.0
Requires:         R-CRAN-RSpectra >= 0.16.0

%description
Tools for spectral clustering of weighted directed networks using motif
adjacency matrices. Methods perform well on large and sparse networks, and
random sampling methods for generating weighted directed networks are also
provided. Based on methodology detailed in Underwood, Elliott and
Cucuringu (2020) <arXiv:2004.01293>.

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
%{rlibdir}/%{packname}/INDEX
