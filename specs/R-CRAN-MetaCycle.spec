%global __brp_check_rpaths %{nil}
%global packname  MetaCycle
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Evaluate Periodicity in Large Scale Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-gnm 
Requires:         R-CRAN-gnm 

%description
There are two functions-meta2d and meta3d for detecting rhythmic signals
from time-series datasets. For analyzing time-series datasets without
individual information, 'meta2d' is suggested, which could incorporates
multiple methods from ARSER, JTK_CYCLE and Lomb-Scargle in the detection
of interested rhythms. For analyzing time-series datasets with individual
information, 'meta3d' is suggested, which takes use of any one of these
three methods to analyze time-series data individual by individual and
gives out integrated values based on analysis result of each individual.

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
