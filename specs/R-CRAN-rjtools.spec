%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjtools
%global packver   1.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          1%{?dist}%{?buildtag}
Summary:          Preparing, Checking, and Submitting Articles to the 'R Journal'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-distill 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-yesno 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-BiocManager 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-distill 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-yesno 
Requires:         R-utils 
Requires:         R-CRAN-tinytex 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-BiocManager 
Requires:         R-CRAN-here 
Requires:         R-CRAN-rmarkdown 

%description
Create an 'R Journal' 'Rmarkdown' template article, that will generate
html and pdf versions of your paper. Check that the paper folder has all
the required components needed for submission. Examples of 'R Journal'
publications can be found at <https://journal.r-project.org>.

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
