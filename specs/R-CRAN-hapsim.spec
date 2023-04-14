%global __brp_check_rpaths %{nil}
%global packname  hapsim
%global packver   0.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.31
Release:          3%{?dist}%{?buildtag}
Summary:          Haplotype Data Simulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Package for haplotype-based genotype simulations. Haplotypes are generated
such that their allele frequencies and linkage disequilibrium coefficients
match those estimated from an input data set.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
