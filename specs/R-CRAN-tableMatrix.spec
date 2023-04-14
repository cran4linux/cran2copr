%global __brp_check_rpaths %{nil}
%global packname  tableMatrix
%global packver   0.82.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.82.0
Release:          3%{?dist}%{?buildtag}
Summary:          Combines 'data.table' and 'matrix' Classes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-data.table 

%description
Provides two classes extending 'data.table' class. Simple 'tableList'
class wraps 'data.table' and any additional structures together. More
complex 'tableMatrix' class combines 'data.table' and 'matrix'. See
<http://github.com/InferenceTechnologies/tableMatrix> for more information
and examples.

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
