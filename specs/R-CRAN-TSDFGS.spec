%global packname  TSDFGS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Training Set Determination for Genomic Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Determining training set for genomic selection using a genetic algorithm
(Holland J.H. (1975) <DOI:10.1145/1216504.1216510>) or simple exchange
algorithm (change an individual every iteration). Three different criteria
are used in both algorithms, which are r-score (Ou J.H., Liao C.T. (2018)
<DOI:10.6342/NTU201802290>), PEV-score (Akdemir D. et al. (2015)
<DOI:10.1186/s12711-015-0116-6>) and CD-score (Laloe D. (1993)
<DOI:10.1186/1297-9686-25-6-557>). Phenotypic data for candidate set is
not necessary for all these methods. By using it, one may readily
determine a training set that can be expected to provide a better training
set comparing to random sampling.

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
%{rlibdir}/%{packname}/libs
