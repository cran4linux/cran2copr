%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DedooseR
%global packver   2.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Monitoring and Analyzing Dedoose Qualitative Data Exports

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-wordcloud2 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-wordcloud2 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-openxlsx 

%description
Streamlines analysis of qualitative data exported from 'Dedoose'
<https://www.dedoose.com>. Supports monitoring thematic saturation,
calculating code frequencies, organizing excerpts, generating dynamic
codebooks, and producing code network maps within 'R'.

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
