%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  whence
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explain Where a Number Came from in 'shiny' Apps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Lets the viewer of a 'shiny' dashboard click a number, a row of a summary
table or a bar of a 'ggplot2' plot, and see where it came from. The
pipeline that makes the result is split into its steps. Each step is run
in turn, and the number of rows after each step is recorded. The result is
an attrition waterfall that shows how many rows each step removed, and
what share of the rows that was, together with code that reproduces the
result. The steps are found from the expression alone, so the pipeline
does not need to be rewritten. The rows that contribute to a result, and
the rows that a step removed, are found only when the viewer asks for
them.

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
