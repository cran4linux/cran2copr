%global packname  MBHdesign
%global packver   1.0.79
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.79
Release:          1%{?dist}
Summary:          Spatial Designs for Ecological and Environmental Surveys

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-class 
Requires:         R-mgcv 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-class 

%description
Provides spatially balanced designs from a set of (contiguous) potential
sampling locations in a study region. Accommodates , without detrimental
effects on spatial balance, sites that the researcher wishes to include in
the survey for reasons other than the current randomisation (legacy
sites).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
