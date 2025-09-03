%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mLLMCelltype
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Cell Type Annotation Using Large Language Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-digest >= 0.6.25
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-digest >= 0.6.25
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Automated cell type annotation for single-cell RNA sequencing data using
consensus predictions from multiple large language models (LLMs). LLMs are
artificial intelligence models trained on vast text corpora to understand
and generate human-like text. This package integrates with 'Seurat'
objects and provides uncertainty quantification for annotations. Supports
various LLM providers including 'OpenAI', 'Anthropic', and 'Google'. The
package leverages these models through their respective APIs (Application
Programming Interfaces) <https://platform.openai.com/docs>,
<https://docs.anthropic.com/>, and
<https://ai.google.dev/gemini-api/docs>. For details see Yang et al.
(2025) <doi:10.1101/2025.04.10.647852>.

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
