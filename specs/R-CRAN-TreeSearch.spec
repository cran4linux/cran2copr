%global packname  TreeSearch
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Phylogenetic Tree Search Using Custom Optimality Criteria

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-phangorn >= 2.2.1
BuildRequires:    R-CRAN-TreeTools >= 1.0.0
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-phangorn >= 2.2.1
Requires:         R-CRAN-TreeTools >= 1.0.0
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Searches for phylogenetic trees that are optimal using a user-defined
criterion. Handles inapplicable data using the algorithm of Brazeau,
Guillerme and Smith (2019) <doi:10.1093/sysbio/syy083>. Implements Profile
Parsimony (Faith and Trueman, 2001) <doi:10.1080/10635150118627>, and
Successive Approximations (Farris, 1969) <doi:10.2307/2412182>.

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
%doc %{rlibdir}/%{packname}/apa-old-doi-prefix.csl
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/preamble.tex
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
