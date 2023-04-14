%global __brp_check_rpaths %{nil}
%global packname  hds
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}%{?buildtag}
Summary:          Hazard Discrimination Summary

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-tensor 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-CRAN-tensor 

%description
Functions for calculating the hazard discrimination summary and its
standard errors, as described in Liang and Heagerty (2016)
<doi:10.1111/biom.12628>.

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
