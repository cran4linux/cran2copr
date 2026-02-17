%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quallmer
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Qualitative Analysis with Large Language Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ellmer >= 0.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-ellmer >= 0.4.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-yardstick 

%description
Tools for AI-assisted qualitative data coding using large language models
('LLMs') via the 'ellmer' package, supporting providers including
'OpenAI', 'Anthropic', 'Google', 'Azure', and local models via 'Ollama'.
Provides a 'codebook'-based workflow for defining coding instructions and
applying them to texts, images, and other data. Includes built-in
'codebooks' for common applications such as sentiment analysis and policy
coding, and functions for creating custom 'codebooks' for specific
research questions. Supports systematic replication across models and
settings, computing inter-coder reliability statistics including
Krippendorff's alpha (Krippendorff 2019, <doi:10.4135/9781071878781>) and
Fleiss' kappa (Fleiss 1971, <doi:10.1037/h0031619>), as well as
gold-standard validation metrics including accuracy, precision, recall,
and F1 scores following Sokolova and Lapalme (2009,
<doi:10.1016/j.ipm.2009.03.002>). Provides audit trail functionality for
documenting coding workflows following Lincoln and Guba's (1985,
ISBN:0803924313) framework for establishing trustworthiness in qualitative
research.

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
