%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rairai
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Model Context Protocol Server for Package Intelligence

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mcplite 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-frontmatter 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-pkgsearch 
BuildRequires:    R-CRAN-treesitter 
BuildRequires:    R-CRAN-treesitter.r 
Requires:         R-CRAN-mcplite 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-frontmatter 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-pkgsearch 
Requires:         R-CRAN-treesitter 
Requires:         R-CRAN-treesitter.r 

%description
Helps artificial intelligence (AI) agents develop 'R' packages more
efficiently and make better-informed code changes. Provides focused,
package-aware context through the Model Context Protocol (MCP) so agents
can understand existing behavior and assess changes with less manual
exploration. Inspects packages without loading or executing their code.

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
