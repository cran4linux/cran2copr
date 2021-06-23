%global __brp_check_rpaths %{nil}
%global packname  hazus
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Damage functions from FEMA's HAZUS software for use in modelingfinancial losses from natural disasters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-reshape2 

%description
Damage Functions (DFs), also known as Vulnerability Functions, associate
the physical damage to a building or a structure (and also its contents
and inventory) from natural disasters to financial damage. The Federal
Emergency Management Agency (FEMA) in USA developed several thousand DFs
and these serve as a benchmark in natural catastrophe modeling, both in
academia and industry. However, these DFs and their documentation are
buried within the HAZUS software are not easily accessible for analysis
and visualization. This package provides more than 1300 raw DFs used by
FEMA's HAZUS software and also functionality to extract and visualize DFs
specific to the flood hazard. The vignette included with this package
demonstrates its use.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
