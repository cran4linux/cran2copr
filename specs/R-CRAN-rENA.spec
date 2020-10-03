%global packname  rENA
%global packver   0.2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1.1
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-concatenate 
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
Requires:         R-CRAN-concatenate 

%description
ENA (Shaffer, D. W. (2017) Quantitative Ethnography. ISBN: 0578191687) is
a method used to identify meaningful and quantifiable patterns in
discourse or reasoning. ENA moves beyond the traditional frequency-based
assessments by examining the structure of the co-occurrence, or
connections in coded data. Moreover, compared to other methodological
approaches, ENA has the novelty of (1) modeling whole networks of
connections and (2) affording both quantitative and qualitative
comparisons between different network models.  Shaffer, D.W., Collier, W.,
& Ruis, A.R. (2016)
<https://learning-analytics.info/index.php/JLA/article/view/4329>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
