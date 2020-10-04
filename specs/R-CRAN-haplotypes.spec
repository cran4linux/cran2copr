%global packname  haplotypes
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Manipulating DNA Sequences and Estimating Unambiguous HaplotypeNetwork with Statistical Parsimony

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-plotrix 

%description
Provides S4 classes and methods for reading and manipulating aligned DNA
sequences, supporting an indel coding methods (only simple indel coding
method is available in the current version), showing base substitutions
and indels, calculating absolute pairwise distances between DNA sequences,
and collapses identical DNA sequences into haplotypes or inferring
haplotypes using user provided absolute pairwise character difference
matrix.  This package also includes S4 classes and methods for estimating
genealogical relationships among haplotypes using statistical parsimony
and plotting parsimony networks.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/example.fas
%{rlibdir}/%{packname}/INDEX
