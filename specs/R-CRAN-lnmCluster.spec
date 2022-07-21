%global __brp_check_rpaths %{nil}
%global packname  lnmCluster
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Logistic Normal Multinomial Clustering for Microbiome Compositional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-pgmm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-pgmm 
Requires:         R-utils 

%description
An implementation of logistic normal multinomial (LNM) clustering. It is
an extension of LNM mixture model proposed by Fang and Subedi (2020)
<arXiv:2011.06682>, and is designed for clustering compositional data. The
package includes 3 extended models: LNM Factor Analyzer (LNM-FA), LNM
Bicluster Mixture Model (LNM-BMM) and Penalized LNM Factor Analyzer
(LNM-FA). There are several advantages of LNM models: 1. LNM provides more
flexible covariance structure; 2. Factor analyzer can reduce the number of
parameters to estimate; 3. Bicluster can simultaneously cluster subjects
and taxa, and provides significant biological insights; 4. Penalty term
allows sparse estimation in the covariance matrix. Details for model
assumptions and interpretation can be found in papers: Tu and Subedi
(2021) <arXiv:2101.01871> and Tu and Subedi (2022)
<doi:10.1002/sam.11555>.

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
