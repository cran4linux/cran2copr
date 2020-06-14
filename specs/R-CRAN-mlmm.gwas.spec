%global packname  mlmm.gwas
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          2%{?dist}
Summary:          Pipeline for GWAS Using MLMM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sommer >= 3.2
BuildRequires:    R-CRAN-coxme >= 2.2.5
BuildRequires:    R-CRAN-multcomp >= 1.4.8
BuildRequires:    R-Matrix >= 1.2.10
BuildRequires:    R-CRAN-multcompView >= 0.1.7
Requires:         R-CRAN-sommer >= 3.2
Requires:         R-CRAN-coxme >= 2.2.5
Requires:         R-CRAN-multcomp >= 1.4.8
Requires:         R-Matrix >= 1.2.10
Requires:         R-CRAN-multcompView >= 0.1.7

%description
Pipeline for Genome-Wide Association Study using Multi-Locus Mixed Model
from Segura V, Vilhjálmsson BJ et al. (2012) <doi:10.1038/ng.2314>. The
pipeline include detection of associated SNPs with MLMM, model selection
by lowest eBIC and p-value threshold, estimation of the effects of the
SNPs in the selected model and graphical functions.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
