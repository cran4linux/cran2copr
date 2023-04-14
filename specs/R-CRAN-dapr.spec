%global __brp_check_rpaths %{nil}
%global packname  dapr
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          'purrr'-Like Apply Functions Over Input Elements

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
An easy-to-use, dependency-free set of functions for iterating over
elements of various input objects. Functions are wrappers around base
apply()/lapply()/vapply() functions but designed to have similar
functionality to the mapping functions in the 'purrr' package
<https://purrr.tidyverse.org/>. Specifically, function names more
explicitly communicate the expected class of the output and functions also
allow for the convenient shortcut of '~ .x' instead of the more verbose
'function(.x) .x'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
