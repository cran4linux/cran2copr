%global __brp_check_rpaths %{nil}
%global packname  EMMREML
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Fitting Mixed Models with Known Covariance Structures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-stats 

%description
The main functions are 'emmreml', and 'emmremlMultiKernel'. 'emmreml'
solves a mixed model with known covariance structure using the 'EMMA'
algorithm.  'emmremlMultiKernel' is a wrapper for 'emmreml' to handle
multiple random components with known covariance structures. The function
'emmremlMultivariate' solves a multivariate gaussian mixed model with
known covariance structure using the 'ECM' algorithm.

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
