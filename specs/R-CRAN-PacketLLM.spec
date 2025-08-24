%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PacketLLM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive 'OpenAI' Model Integration in 'RStudio'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-readtext 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-future 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-readtext 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Offers an interactive 'RStudio' gadget interface for communicating with
'OpenAI' large language models (e.g., 'gpt-5', 'gpt-5-mini', 'gpt-5-nano')
(<https://platform.openai.com/docs/api-reference>). Enables users to
conduct multiple chat conversations simultaneously in separate tabs.
Supports uploading local files (R, PDF, DOCX) to provide context for the
models. Allows per-conversation configuration of system messages (where
supported by the model). API interactions via the 'httr' package are
performed asynchronously using 'promises' and 'future' to avoid blocking
the R console. Useful for tasks like code generation, text summarization,
and document analysis directly within the 'RStudio' environment. Requires
an 'OpenAI' API key set as an environment variable.

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
