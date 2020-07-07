%global packname  iterpc
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}
Summary:          Efficient Iterator for Permutations and Combinations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrangements >= 1.0.0
BuildRequires:    R-CRAN-gmp >= 0.5.12
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-arrangements >= 1.0.0
Requires:         R-CRAN-gmp >= 0.5.12
Requires:         R-CRAN-iterators 

%description
Iterator for generating permutations and combinations. They can be either
drawn with or without replacement, or with distinct/ non-distinct items
(multiset). The generated sequences are in lexicographical order
(dictionary order). The algorithms to generate permutations and
combinations are memory efficient. These iterative algorithms enable users
to process all sequences without putting all results in the memory at the
same time. The algorithms are written in C/C++ for faster performance.
Note: 'iterpc' is no longer being maintained. Users are recommended to
switch to 'arrangements'.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
