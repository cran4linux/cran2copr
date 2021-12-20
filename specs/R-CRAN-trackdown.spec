%global __brp_check_rpaths %{nil}
%global packname  trackdown
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Collaborative Editing of Rmd (or Rnw) Documents in Google Drive

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-googledrive > 1.0.1
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-googledrive > 1.0.1
Requires:         R-CRAN-rmarkdown 

%description
Collaborative writing and editing of R Markdown (or Sweave) documents. The
local .Rmd (or .Rnw) is uploaded as a plain-text file to Google Drive. By
taking advantage of the easily readable Markdown (or LaTeX) syntax and the
well-known online interface offered by Google Docs, collaborators can
easily contribute to the writing and editing process. After integrating
all authors’ contributions, the final document can be downloaded and
rendered locally.

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
