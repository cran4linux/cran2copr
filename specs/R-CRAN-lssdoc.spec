%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lssdoc
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          'LimeSurvey' '.lss' Questionnaires to and from Word Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xml2 

%description
Turn a 'LimeSurvey' '.lss' survey export into a publication-quality
questionnaire document in Word ('.docx') or PDF, with up to four of the
survey's own languages side by side. Every label the package adds around
that content -- column headers, type names, the audit section -- is
written in English, French, German, Spanish or Italian, whatever the
survey languages are. A rule-based audit flags missing translations,
forward filter references, duplicate codes, array-scale inconsistencies
and orphan structural references. Questionnaires travel the other way too:
describe one in R, or fill in a Word form, and write a '.lss' file ready
to import. Meant for the people who work on questionnaires -- researchers,
methodologists, ethics committees, translators and reviewers -- and fully
local: the source file is the only input, and no questionnaire content is
uploaded to a third-party service.

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
