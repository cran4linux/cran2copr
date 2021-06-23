%global __brp_check_rpaths %{nil}
%global packname  RHPCBenchmark
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Benchmarks for High-Performance Computing Environments

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-cluster 
BuildRequires:    R-Matrix 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-cluster 
Requires:         R-Matrix 

%description
Microbenchmarks for determining the run time performance of aspects of the
R programming environment and packages relevant to high-performance
computation.  The benchmarks are divided into three categories: dense
matrix linear algebra kernels, sparse matrix linear algebra kernels, and
machine learning functionality.

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
