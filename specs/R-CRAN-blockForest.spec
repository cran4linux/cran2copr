%global packname  blockForest
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}
Summary:          Block Forests: Random Forests for Blocks of Clinical and OmicsCovariate Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-survival 

%description
A random forest variant 'block forest' ('BlockForest') tailored to the
prediction of binary, survival and continuous outcomes using
block-structured covariate data, for example, clinical covariates plus
measurements of a certain omics data type or multi-omics data, that is,
data for which measurements of different types of omics data and/or
clinical data for each patient exist. Examples of different omics data
types include gene expression measurements, mutation data and copy number
variation measurements. Block forest are presented in Hornung & Wright
(2019). The package includes four other random forest variants for
multi-omics data: 'RandomBlock', 'BlockVarSel', 'VarProb', and
'SplitWeights'. These were also considered in Hornung & Wright (2019), but
performed worse than block forest in their comparison study based on 20
real multi-omics data sets. Therefore, we recommend to use block forest
('BlockForest') in applications. The other random forest variants can,
however, be consulted for academic purposes, for example, in the context
of further methodological developments. Reference: Hornung, R. & Wright,
M. N. (2019) Block Forests: random forests for blocks of clinical and
omics covariate data. BMC Bioinformatics 20:358.
<doi:10.1186/s12859-019-2942-y>.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
