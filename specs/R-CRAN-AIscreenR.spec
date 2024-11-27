%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIscreenR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          AI Screening Tools in R for Systematic Reviewing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-askpass 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-askpass 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-jsonlite 

%description
Provides functions to conduct title and abstract screening in systematic
reviews using large language models, such as the Generative Pre-trained
Transformer (GPT) models from 'OpenAI' <https://platform.openai.com/>.
These functions can enhance the quality of title and abstract screenings
while reducing the total screening time significantly. In addition, the
package includes tools for quality assessment of title and abstract
screenings, as described in Vembye, Christensen, Mølgaard, and Schytt
(2024) <DOI:10.31219/osf.io/yrhzm>.

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
