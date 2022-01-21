%global __brp_check_rpaths %{nil}
%global packname  sweater
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Speedy Word Embedding Association Test and Extras Using R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-LiblineaR 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-LiblineaR 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cli 

%description
Conduct various tests for evaluating implicit biases in word embeddings:
Word Embedding Association Test (Caliskan et al., 2017),
<doi:10.1126/science.aal4230>, Relative Norm Distance (Garg et al., 2018),
<doi:10.1073/pnas.1720347115>, Mean Average Cosine Similarity (Mazini et
al., 2019) <arXiv:1904.04047>, SemAxis (An et al., 2018)
<arXiv:1806.05521>, Relative Negative Sentiment Bias (Sweeney & Najafian,
2019) <doi:10.18653/v1/P19-1162>, and Embedding Coherence Test (Dev &
Phillips, 2019) <arXiv:1901.07656>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
