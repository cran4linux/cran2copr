%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tarpolyglot
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Run 'Python', 'Julia', 'Rust', and 'C++' Inside 'targets' Pipeline Steps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-targets 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-JuliaCall 
BuildRequires:    R-CRAN-crew 
BuildRequires:    R-CRAN-rextendr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-targets 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-JuliaCall 
Requires:         R-CRAN-crew 
Requires:         R-CRAN-rextendr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-cli 

%description
Adds target constructors that make it easy to use 'Python', 'Julia',
'Rust', and 'C++' inside a 'targets' pipeline using 'reticulate',
'JuliaCall', 'rextendr', and 'Rcpp'. Provides tar_target_py(),
tar_target_jl(), tar_target_rs(), and tar_target_cpp() (with matching
_raw() variants), each mirroring 'targets' tar_target() and
tar_target_raw() functions. 'Python' and 'Julia' steps run a script via a
live interpreter with optional R pre- and post-scripts; 'Rust' and 'C++'
steps compile functions and call them from an R post-script. Results are
then returned either as converted R objects or as files written to disk
(format = "file"). Dynamic branching, environment/version selection, a
'crew' controller for isolation, and the full set of tar_target_raw()
arguments are supported.

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
