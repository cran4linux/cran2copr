%global packname  arrow
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Integration to 'Apache' 'Arrow'

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-bit64 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
'Apache' 'Arrow' <https://arrow.apache.org/> is a cross-language
development platform for in-memory data. It specifies a standardized
language-independent columnar memory format for flat and hierarchical
data, organized for efficient analytic operations on modern hardware. This
package provides an interface to the 'Arrow C++' library.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
