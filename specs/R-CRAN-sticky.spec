%global __brp_check_rpaths %{nil}
%global packname  sticky
%global packver   0.5.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Persist Attributes Across Data Operations

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
In base R, object attributes are lost when objects are modified by common
data operations such as subset, filter, slice, append, extract etc. This
packages allows objects to be marked as 'sticky' and have attributes
persisted during these operations or when inserted into or extracted from
list-like or table-like objects.

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
