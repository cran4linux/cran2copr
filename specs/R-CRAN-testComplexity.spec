%global packname  testComplexity
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Asymptotic Complexity Testing Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 2.1.0
BuildRequires:    R-boot 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-bench 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-testthat >= 2.1.0
Requires:         R-boot 
Requires:         R-utils 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-bench 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
It classifies the asymptotic time/memory complexity class for an
algorithm/function through the complexity classifiers, with data frames
returned by the quantifiers. The data frames can be passed onto the
plotting functions for obtaining a visual description of the benchmarks
against data sizes if the user intends to diagnose the trend via the
traditional method. For testing the algorithm against an expected time
complexity class, the user can directly use the expect functions. Please
check
<https://anirban166.github.io/testComplexity/articles/testComplexity> to
get started.

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
