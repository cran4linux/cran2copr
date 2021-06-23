%global __brp_check_rpaths %{nil}
%global packname  CJAMP
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Copula-Based Joint Analysis of Multiple Phenotypes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
Requires:         R-stats 
Requires:         R-CRAN-optimx 

%description
We provide a computationally efficient and robust implementation of the
recently proposed C-JAMP (Copula-based Joint Analysis of Multiple
Phenotypes) method (Konigorski et al., 2019, submitted). C-JAMP allows
estimating and testing the association of one or multiple predictors on
multiple outcomes in a joint model, and is implemented here with a focus
on large-scale genome-wide association studies with two phenotypes. The
use of copula functions allows modeling a wide range of multivariate
dependencies between the phenotypes, and previous results are supporting
that C-JAMP can increase the power of association studies to identify
associated genetic variants in comparison to existing methods (Konigorski,
Yilmaz, Pischon, 2016, <DOI:10.1186/s12919-016-0045-6>; Konigorski,
Yilmaz, Bull, 2014, <DOI:10.1186/1753-6561-8-S1-S72>). In addition to the
C-JAMP functions, functions are available to generate genetic and
phenotypic data, to compute the minor allele frequency (MAF) of genetic
markers, and to estimate the phenotypic variance explained by genetic
markers.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
