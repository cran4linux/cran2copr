%global packname  noia
%global packver   0.97.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.97.1
Release:          3%{?dist}
Summary:          Implementation of the Natural and Orthogonal InterAction (NOIA)model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The NOIA model, as described extensively in Alvarez-Castro & Carlborg
(2007), is a framework facilitating the estimation of genetic effects and
genotype-to-phenotype maps. This package provides the basic tools to
perform linear and multilinear regressions from real populations (provided
the phenotype and the genotype of every individuals), estimating the
genetic effects from different reference points, the genotypic values, and
the decomposition of genetic variances in a multi-locus, 2 alleles system.
This package is presented in Le Rouzic & Alvarez-Castro (2008).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
