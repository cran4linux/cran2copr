%global __brp_check_rpaths %{nil}
%global packname  DAKS
%global packver   2.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Data Analysis and Knowledge Spaces

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-relations 
BuildRequires:    R-CRAN-sets 
Requires:         R-CRAN-relations 
Requires:         R-CRAN-sets 

%description
Functions and an example dataset for the psychometric theory of knowledge
spaces.  This package implements data analysis methods and procedures for
simulating data and quasi orders and transforming different formulations
in knowledge space theory.  See package?DAKS for an overview.

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
