%global packname  rENA
%global packver   0.2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.1
Release:          3%{?dist}
Summary:          Epistemic Network Analysis

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-magrittr 

%description
ENA (Shaffer, D. W. (2017) Quantitative Ethnography. ISBN: 0578191687) is
a method used to identify meaningful and quantifiable patterns in
discourse or reasoning. ENA moves beyond the traditional frequency-based
assessments by examining the structure of the co-occurrence, or
connections in coded data. Moreover, compared to other methodological
approaches, ENA has the novelty of (1) modeling whole networks of
connections and (2) affording both quantitative and qualitative
comparisons between different network models.  Shaffer, D.W., Collier, W.,
& Ruis, A.R. (2016) <doi:10.18608/jla.2016.33.3>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/rmd
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
