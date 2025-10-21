%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arete
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated REtrieval from TExt

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-cld2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-fedmatch 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gecko 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-cld2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-fedmatch 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gecko 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-rmarkdown 

%description
A Python based pipeline for extraction of species occurrence data through
the usage of large language models. Includes validation tools designed to
handle model hallucinations for a scientific, rigorous use of LLM.
Currently supports usage of GPT with more planned, including local and
non-proprietary models. For more details on the methodology used please
consult the references listed under each function, such as Kent, A. et al.
(1995) <doi:10.1002/asi.5090060209>, van Rijsbergen, C.J. (1979,
ISBN:978-0408709293, Levenshtein, V.I. (1966)
<https://nymity.ch/sybilhunting/pdf/Levenshtein1966a.pdf> and Klaus
Krippendorff (2011)
<https://repository.upenn.edu/handle/20.500.14332/2089>.

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
