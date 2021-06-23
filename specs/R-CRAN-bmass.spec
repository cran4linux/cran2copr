%global __brp_check_rpaths %{nil}
%global packname  bmass
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Multivariate Analysis of Summary Statistics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-stats 

%description
Multivariate tool for analyzing genome-wide association study results in
the form of univariate summary statistics. The goal of 'bmass' is to
comprehensively test all possible multivariate models given the phenotypes
and datasets provided. Multivariate models are determined by assigning
each phenotype to being either Unassociated (U), Directly associated (D)
or Indirectly associated (I) with the genetic variant of interest. Test
results for each model are presented in the form of Bayes factors, thereby
allowing direct comparisons between models. The underlying framework
implemented here is based on the modeling developed in "A Unified
Framework for Association Analysis with Multiple Related Phenotypes", M.
Stephens (2013) <doi:10.1371/journal.pone.0065245>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
