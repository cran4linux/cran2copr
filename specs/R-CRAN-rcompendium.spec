%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcompendium
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Create a Package or Research Compendium Structure

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cffr 
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-cffr 
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-usethis 
Requires:         R-utils 
Requires:         R-CRAN-xfun 

%description
Makes easier the creation of R package or research compendium (i.e. a
predefined files/folders structure) so that users can focus on the
code/analysis instead of wasting time organizing files. A full
ready-to-work structure is set up with some additional features: version
control, remote repository creation, CI/CD configuration (check package
integrity under several OS, test code with 'testthat', and build and
deploy website using 'pkgdown'). This package heavily relies on the R
packages 'devtools' and 'usethis' and follows recommendations made by
Wickham H. (2015) <ISBN:9781491910597> and Marwick B. et al. (2018)
<doi:10.7287/peerj.preprints.3192v2>.

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
