%global packname  targets
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Function-Oriented 'Make'-Like Declarative Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.4.3
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-igraph >= 1.2.5
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-digest >= 0.6.25
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-vctrs >= 0.2.4
BuildRequires:    R-CRAN-codetools >= 0.2.16
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr >= 3.4.3
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-igraph >= 1.2.5
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-digest >= 0.6.25
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-vctrs >= 0.2.4
Requires:         R-CRAN-codetools >= 0.2.16
Requires:         R-stats 
Requires:         R-utils 

%description
As a pipeline toolkit for Statistics and data science in R, the 'targets'
package brings together function-oriented programming and 'Make'-like
declarative workflows. It analyzes the dependency relationships among the
tasks of a workflow, skips steps that are already up to date, runs the
necessary computation with optional parallel workers, abstracts files as R
objects, and provides tangible evidence that the results match the
underlying code and data. The methodology in this package borrows from GNU
'Make' (2015, ISBN:978-9881443519) and 'drake' (2018,
<doi:10.21105/joss.00550>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
