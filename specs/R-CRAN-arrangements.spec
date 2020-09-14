%global packname  arrangements
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Generators and Iterators for Permutations, Combinations, Integer Partitions and Compositions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel >= 4.2.3
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-R6 

%description
Fast generators and iterators for permutations, combinations, integer
partitions and compositions. The arrangements are in lexicographical order
and generated iteratively in a memory efficient manner. It has been
demonstrated that 'arrangements' outperforms most existing packages of
similar kind. Benchmarks could be found at
<https://randy3k.github.io/arrangements/articles/benchmark.html>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
