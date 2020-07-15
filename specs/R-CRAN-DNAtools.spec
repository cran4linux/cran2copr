%global packname  DNAtools
%global packver   0.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Tools for Analysing Forensic Genetic DNA Data

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppParallel >= 4.3.20
BuildRequires:    R-CRAN-Rsolnp >= 1.16
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-multicool >= 0.1.10
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-RcppParallel >= 4.3.20
Requires:         R-CRAN-Rsolnp >= 1.16
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-multicool >= 0.1.10

%description
Computationally efficient tools for comparing all pairs of profiles in a
DNA database. The expectation and covariance of the summary statistic is
implemented for fast computing. Routines for estimating proportions of
close related individuals are available. The use of wildcards (also called
F- designation) is implemented. Dedicated functions ease plotting the
results. See Tvedebrink et al. (2012) <doi:10.1016/j.fsigen.2011.08.001>.
Compute the distribution of the numbers of alleles in DNA mixtures. See
Tvedebrink (2013) <doi:10.1016/j.fsigss.2013.10.142>.

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
