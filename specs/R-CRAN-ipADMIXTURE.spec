%global __brp_check_rpaths %{nil}
%global packname  ipADMIXTURE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Iterative Pruning Population Admixture Inference Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-treemap 
BuildRequires:    R-CRAN-ape 
Requires:         R-stats 
Requires:         R-CRAN-treemap 
Requires:         R-CRAN-ape 

%description
A data clustering package based on admixture ratios (Q matrix) of
population structure. The framework is based on iterative Pruning
procedure that performs data clustering by splitting a given population
into subclusters until meeting the condition of stopping criteria the same
as ipPCA, iNJclust, and IPCAPS frameworks. The package also provides a
function to retrieve phylogeny tree that construct a neighbor-joining tree
based on a similar matrix between clusters. By given multiple Q matrices
with varying a number of ancestors (K), the framework define a similar
value between clusters i,j as a minimum number K* that makes majority of
members of two clusters are in the different clusters. This K* reflexes a
minimum number of ancestors we need to splitting cluster i,j into
different clusters if we assign K* clusters based on maximum admixture
ratio of individuals. The publication of this package is at Chainarong
Amornbunchornvej, Pongsakorn Wangkumhang, and Sissades Tongsima (2020)
<doi:10.1101/2020.03.21.001206>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ipADMIXTURE_0.1.0.pdf
%{rlibdir}/%{packname}/INDEX
