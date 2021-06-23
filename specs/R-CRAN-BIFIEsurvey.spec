%global __brp_check_rpaths %{nil}
%global packname  BIFIEsurvey
%global packver   3.3-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.12
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Survey Statistics in Educational Assessment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-miceadds 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-miceadds 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains tools for survey statistics (especially in educational
assessment) for datasets with replication designs (jackknife, bootstrap,
replicate weights; see Kolenikov, 2010; Pfefferman & Rao, 2009a, 2009b,
<doi:10.1016/S0169-7161(09)70003-3>, <doi:10.1016/S0169-7161(09)70037-9>);
Shao, 1996, <doi:10.1080/02331889708802523>). Descriptive statistics,
linear and logistic regression, path models for manifest variables with
measurement error correction and two-level hierarchical regressions for
weighted samples are included. Statistical inference can be conducted for
multiply imputed datasets and nested multiply imputed datasets and is in
particularly suited for the analysis of plausible values (for details see
George, Oberwimmer & Itzlinger-Bruneforth, 2016; Bruneforth, Oberwimmer &
Robitzsch, 2016; Robitzsch, Pham & Yanagida, 2016;
<doi:10.17888/fdb-demo:bistE813I-16a>). The package development was
supported by BIFIE (Federal Institute for Educational Research, Innovation
and Development of the Austrian School System; Salzburg, Austria).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
