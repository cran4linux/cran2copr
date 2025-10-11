%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apathe
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          American Psychological Association Thesis Templates for R Markdown

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmdfiltr >= 0.1.5
BuildRequires:    R-CRAN-papaja >= 0.1.3
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-rmdfiltr >= 0.1.5
Requires:         R-CRAN-papaja >= 0.1.3
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-assertthat 

%description
Facilitates writing computationally reproducible student theses in PDF
format that conform to the American Psychological Association (APA)
manuscript guidelines (6th Edition). The package currently provides two R
Markdown templates for homework and theses at the Psychology Department of
the University of Cologne. The package builds on the package 'papaja' but
is tailored to the requirements of student theses and omits features for
simplicity.

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
