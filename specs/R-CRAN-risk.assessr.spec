%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  risk.assessr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Package Risk Metrics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rcmdcheck 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rcmdcheck 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-jsonlite 

%description
Provides a structured approach to assess the quality and trustworthiness
of R packages (documentation, testing, popularity, dependencies),
supporting informed decisions in production or research by highlighting
strengths and potential risks in adoption or development.

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
