%global __brp_check_rpaths %{nil}
%global packname  hsphase
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Phasing, Pedigree Reconstruction, Sire Imputation andRecombination Events Identification of Half-sib Families UsingSNP Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.4.300.8.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-snowfall 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-Rcpp >= 0.11.2

%description
Identification of recombination events, haplotype reconstruction, sire
imputation and pedigree reconstruction using half-sib family SNP data.

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
