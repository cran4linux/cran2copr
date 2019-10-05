%global packname  arrangements
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Fast Generators and Iterators for Permutations, Combinations andPartitions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel >= 4.2.3
Requires:         gmp
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-gmp 

%description
Fast generators and iterators for permutations, combinations and
partitions. The iterators allow users to generate arrangements in a memory
efficient manner and the generated arrangements are in lexicographical
(dictionary) order. Permutations and combinations can be drawn
with/without replacement and support multisets. It has been demonstrated
that 'arrangements' outperforms most of the existing packages of similar
kind. Some benchmarks could be found at
<https://randy3k.github.io/arrangements/articles/benchmark.html>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
