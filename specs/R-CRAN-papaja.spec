%global __brp_check_rpaths %{nil}
%global packname  papaja
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prepare American Psychological Association Journal Articles with R Markdown

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.4
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.26
BuildRequires:    R-CRAN-bookdown >= 0.9
BuildRequires:    R-CRAN-broom >= 0.7.0
BuildRequires:    R-CRAN-rmdfiltr >= 0.1.3
BuildRequires:    R-CRAN-tinylabels >= 0.1.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-rmarkdown >= 2.4
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-knitr >= 1.26
Requires:         R-CRAN-bookdown >= 0.9
Requires:         R-CRAN-broom >= 0.7.0
Requires:         R-CRAN-rmdfiltr >= 0.1.3
Requires:         R-CRAN-tinylabels >= 0.1.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-zip 

%description
Tools to create dynamic, submission-ready manuscripts, which conform to
American Psychological Association manuscript guidelines. We provide R
Markdown document formats for manuscripts (PDF and Word) and revision
letters (PDF). Helper functions facilitate reporting statistical analyses
or create publication-ready tables and plots.

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
