%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gptzeror
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Text Written by Large Language Models using 'GPTZero'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tidyr 

%description
An R interface to the 'GPTZero' API (<https://gptzero.me/docs>). Allows
users to classify text into human and computer written with probabilities.
Formats the data into data frames where each sentence is an observation.
Paragraph-level and document-level predictions are organized to align with
the sentences.

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
