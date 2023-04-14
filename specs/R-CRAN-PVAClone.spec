%global __brp_check_rpaths %{nil}
%global packname  PVAClone
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Population Viability Analysis with Data Cloning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dcmle >= 0.3.0
BuildRequires:    R-CRAN-dclone 
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-dcmle >= 0.3.0
Requires:         R-CRAN-dclone 
Requires:         R-stats4 
Requires:         R-methods 
Requires:         R-CRAN-coda 

%description
Likelihood based population viability analysis in the presence of
observation error and missing data. The package can be used to fit,
compare, predict, and forecast various growth model types using data
cloning.

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
