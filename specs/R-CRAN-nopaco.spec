%global __brp_check_rpaths %{nil}
%global packname  nopaco
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Parametric Concordance Coefficient

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.1.5
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-Matrix >= 1.1.5
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 

%description
A non-parametric test for multi-observer concordance and differences
between concordances in (un)balanced data.

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
