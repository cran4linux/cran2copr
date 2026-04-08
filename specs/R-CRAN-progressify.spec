%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  progressify
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Progress Reporting of Common Functions via One Magic Function

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-methods 
Requires:         R-CRAN-progressr 
Requires:         R-methods 

%description
The progressify() function rewrites (transpiles) calls to sequential and
parallel map-reduce functions such as base::lapply(), purrr::map(),
foreach::foreach(), and plyr::llply() to signal progress updates. By
combining this function with R's native pipe operator, you have a
straightforward way to report progress on iterative computations with
minimal refactoring, e.g. 'lapply(x, fcn) |> progressify()' and
'purrr::map(x, fcn) |> progressify()'. It is compatible with the
'futurize' package for parallelization, e.g. 'lapply(x, fcn) |>
progressify() |> futurize()' and 'purrr::map(x, fcn) |> futurize() |>
progressify()'.

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
