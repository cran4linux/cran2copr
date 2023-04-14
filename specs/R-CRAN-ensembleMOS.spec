%global __brp_check_rpaths %{nil}
%global packname  ensembleMOS
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          3%{?dist}%{?buildtag}
Summary:          Ensemble Model Output Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ensembleBMA 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-evd 
Requires:         R-CRAN-ensembleBMA 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-evd 

%description
Ensemble Model Output Statistics to create probabilistic forecasts from
ensemble forecasts and weather observations.

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
