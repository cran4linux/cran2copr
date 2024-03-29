%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  openai
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Wrapper for OpenAI API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-httr >= 1.4.3
BuildRequires:    R-CRAN-lifecycle >= 1.0.1
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-httr >= 1.4.3
Requires:         R-CRAN-lifecycle >= 1.0.1
Requires:         R-CRAN-assertthat >= 0.2.1

%description
An R wrapper of OpenAI API endpoints (see
<https://platform.openai.com/docs/introduction> for details). This package
covers Models, Completions, Chat, Edits, Images, Embeddings, Audio, Files,
Fine-tunes, Moderations, and legacy Engines endpoints.

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
