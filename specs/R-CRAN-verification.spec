%global __brp_check_rpaths %{nil}
%global packname  verification
%global packver   1.42
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.42
Release:          3%{?dist}%{?buildtag}
Summary:          Weather Forecast Verification Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-fields 
Requires:         R-boot 
Requires:         R-CRAN-CircStats 
Requires:         R-MASS 
Requires:         R-CRAN-dtw 
Requires:         R-graphics 
Requires:         R-stats 

%description
Utilities for verifying discrete, continuous and probabilistic forecasts,
and forecasts expressed as parametric distributions are included.

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
