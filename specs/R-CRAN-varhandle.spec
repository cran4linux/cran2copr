%global __brp_check_rpaths %{nil}
%global packname  varhandle
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Robust Variable Handling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-utils 
Requires:         R-graphics 

%description
Variables are the fundamental parts of each programming language but
handling them efficiently might be frustrating for programmers. This
package contains some functions to help user (especially data explorers)
to make more sense of their variables and take the most out of variables
and hardware resources. These functions are written, collected and crafted
over 7 years of experience in statistical data analysis on
high-dimensional data, and for each of them there was a need. Functions in
this package are suppose to be efficient and easy to use, hence they will
be frequently updated to make them more convenient.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
