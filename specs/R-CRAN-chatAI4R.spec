%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chatAI4R
%global packver   0.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Chat-Based Interactive Artificial Intelligence for R

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-deepRstudio 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-future 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-deepRstudio 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 

%description
The Large Language Model (LLM) represents a groundbreaking advancement in
data science and programming, and also allows us to extend the world of R.
A seamless interface for integrating the 'OpenAI' Web APIs into R is
provided in this package. This package leverages LLM-based AI techniques,
enabling efficient knowledge discovery and data analysis (see 'OpenAI' Web
APIs details <https://openai.com/blog/openai-api>). The previous functions
such as seamless translation and image generation have been moved to other
packages 'deepRstudio' and 'stableDiffusion4R'.

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
