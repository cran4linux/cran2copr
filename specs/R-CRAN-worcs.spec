%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  worcs
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Workflow for Open Reproducible Code in Science

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-prereg >= 0.6.0
BuildRequires:    R-CRAN-rticles >= 0.25
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-CRAN-credentials 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-gh 
Requires:         R-CRAN-prereg >= 0.6.0
Requires:         R-CRAN-rticles >= 0.25
Requires:         R-methods 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-tinytex 
Requires:         R-CRAN-credentials 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-gh 

%description
Create reproducible and transparent research projects in 'R'. This package
is based on the Workflow for Open Reproducible Code in Science (WORCS), a
step-by-step procedure based on best practices for Open Science. It
includes an 'RStudio' project template, several convenience functions, and
all dependencies required to make your project reproducible and
transparent. WORCS is explained in the tutorial paper by Van Lissa,
Brandmaier, Brinkman, Lamprecht, Struiksma, & Vreede (2021).
<doi:10.3233/DS-210031>.

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
