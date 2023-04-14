%global __brp_check_rpaths %{nil}
%global packname  tdsc
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Time Domain Signal Coding

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-moments 

%description
Functions for performing time domain signal coding as used in Chesmore
(2001) <doi:10.1016/S0003-682X(01)00009-3>, and related tasks. This
package creates the standard S-matrix and A-matrix (with variable lag),
has tools to convert coding matrices into distributed matrices, provides
published codebooks and allows for extraction of code sequences.

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
