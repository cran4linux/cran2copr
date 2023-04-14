%global __brp_check_rpaths %{nil}
%global packname  denseFLMM
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Functional Linear Mixed Models for Densely Sampled Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-mgcv >= 1.8.12
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-mgcv >= 1.8.12
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 

%description
Estimation of functional linear mixed models for densely sampled data
based on functional principal component analysis.

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
