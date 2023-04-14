%global __brp_check_rpaths %{nil}
%global packname  CatDyn
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Fishery Stock Assessment by Catch Dynamics Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-optimx >= 2013.8.6
BuildRequires:    R-CRAN-BB 
Requires:         R-CRAN-optimx >= 2013.8.6
Requires:         R-CRAN-BB 

%description
Based on fishery Catch Dynamics instead of fish Population Dynamics (hence
CatDyn) and using high-frequency or medium-frequency catch in biomass or
numbers, fishing nominal effort, and mean fish body weight by time step,
from one or two fishing fleets, estimate stock abundance, natural
mortality rate, and fishing operational parameters. It includes methods
for data organization, plotting standard exploratory and analytical plots,
predictions, for 100 types of models of increasing complexity, and 72
likelihood models for the data.

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
