%global __brp_check_rpaths %{nil}
%global packname  dialectR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Doing Dialectometry in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-ggvoronoi 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-ggvoronoi 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-tibble 

%description
Quantitative approaches to dialectology based primarily on modifications
of edit distance, which is more commonly known as the field of
dialectometry. For further reference on the school of thought associated
with these methods, see Wieling & Nerbonne (2015),
<https://www.annualreviews.org/doi/10.1146/annurev-linguist-030514-124930>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
