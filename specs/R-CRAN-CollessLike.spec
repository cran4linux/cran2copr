%global packname  CollessLike
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Distribution and Percentile of Sackin, Cophenetic andColless-Like Balance Indices of Phylogenetic Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-igraph 

%description
Computation of Colless-Like, Sackin and cophenetic balance indices of a
phylogenetic tree and study of the distribution of these balance indices
under the alpha-gamma model. For more details see A. Mir, F. Rossello, L.
Rotger (2013) <doi:10.1016/j.mbs.2012.10.005> and (2018)
<doi:10.1371/journal.pone.0203401>, M. J. Sackin (1972)
<doi:10.1093/sysbio/21.2.225>, D. H. Colless (1982) <doi:10.2307/2413420>.

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
%{rlibdir}/%{packname}/INDEX
