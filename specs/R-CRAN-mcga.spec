%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcga
%global packver   3.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Coded Genetic Algorithms for Real-Valued Optimization Problems

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-GA 
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-GA 

%description
Machine coded genetic algorithm (MCGA) is a fast tool for real-valued
optimization problems. It uses the byte representation of variables rather
than real-values. It performs the classical crossover operations (uniform)
on these byte representations. Mutation operator is also similar to
classical mutation operator, which is to say, it changes a randomly
selected byte value of a chromosome by +1 or -1 with probability 1/2. In
MCGAs there is no need for encoding-decoding process and the classical
operators are directly applicable on real-values. It is fast and can
handle a wide range of a search space with high precision. Using a
256-unary alphabet is the main disadvantage of this algorithm but a
moderate size population is convenient for many problems. Package also
includes multi_mcga function for multi objective optimization problems.
This function sorts the chromosomes using their ranks calculated from the
non-dominated sorting algorithm.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
