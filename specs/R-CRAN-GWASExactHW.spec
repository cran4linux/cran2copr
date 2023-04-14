%global __brp_check_rpaths %{nil}
%global packname  GWASExactHW
%global packver   1.01
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.01
Release:          3%{?dist}%{?buildtag}
Summary:          Exact Hardy-Weinburg testing for Genome Wide Association Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
This package contains a function to do exact Hardy-Weinburg testing (using
Fisher's test) for SNP genotypes as typically obtained in a Genome Wide
Association Study (GWAS).

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
