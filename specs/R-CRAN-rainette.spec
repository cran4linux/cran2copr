%global __brp_check_rpaths %{nil}
%global packname  rainette
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          The Reinert Method for Textual Data Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-quanteda >= 2.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-quanteda.textstats 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-ggwordcloud 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-quanteda >= 2.1
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-quanteda.textstats 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-ggwordcloud 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-progressr 

%description
An R implementation of the Reinert text clustering method. For more
details about the algorithm see the included vignettes or Reinert (1990)
<doi:10.1177/075910639002600103>.

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
