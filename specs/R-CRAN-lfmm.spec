%global packname  lfmm
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Latent Factor Mixed Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 

%description
Fast and accurate inference of gene-environment associations (GEA) in
genome-wide studies (Caye et al., 2019, <doi:10.1093/molbev/msz008>). We
developed a least-squares estimation approach for confounder and effect
sizes estimation that provides a unique framework for several categories
of genomic data, not restricted to genotypes. The speed of the new
algorithm is several times faster than the existing GEA approaches, then
our previous version of the 'LFMM' program present in the 'LEA' package
(Frichot and Francois, 2015, <doi:10.1111/2041-210X.12382>).

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
