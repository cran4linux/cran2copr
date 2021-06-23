%global __brp_check_rpaths %{nil}
%global packname  RCPmod
%global packver   2.190
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.190
Release:          3%{?dist}%{?buildtag}
Summary:          Regions of Common Profiles Modelling with Mixtures-of-Experts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet >= 2.0.13
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-fishMod 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-glmnet >= 2.0.13
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-fishMod 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 

%description
Identifies regions of common (species) profiles (RCPs), possibly when
sampling artefacts are present.  Within a region the probability of
sampling all species remains approximately constant.  This is performed
using mixtures-of-experts models.  The package also contains associated
methods, such as diagnostics.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
