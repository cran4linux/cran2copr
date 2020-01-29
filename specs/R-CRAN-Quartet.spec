%global packname  Quartet
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Comparison of Phylogenetic Trees Using Quartet and SplitMeasures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Ternary >= 1.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-TreeTools 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Ternary >= 1.0
Requires:         R-CRAN-ape 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-TreeTools 

%description
Calculates the number of four-taxon subtrees consistent with a pair of
cladograms, calculating the symmetric quartet distance of Bandelt & Dress
(1986), Reconstructing the shape of a tree from observed dissimilarity
data, Advances in Applied Mathematics, 7, 309-343
<doi:10.1016/0196-8858(86)90038-2>, and using the tqDist algorithm of Sand
et al. (2014), tqDist: a library for computing the quartet and triplet
distances between binary or general trees, Bioinformatics, 30, 2079–2080
<doi:10.1093/bioinformatics/btu157> for pairs of binary trees.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Get_stuck_in.md
%doc %{rlibdir}/%{packname}/preamble.tex
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/trees
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
