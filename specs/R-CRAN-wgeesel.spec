%global packname  wgeesel
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Weighted Generalized Estimating Equations and Model Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-bindata 
BuildRequires:    R-CRAN-PoisNor 
BuildRequires:    R-CRAN-CRTgeeDR 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-bindata 
Requires:         R-CRAN-PoisNor 
Requires:         R-CRAN-CRTgeeDR 

%description
Weighted generalized estimating equations (WGEE) is an extension of
generalized linear models to longitudinal clustered data by incorporating
the correlation within-cluster when data is missing at random (MAR). The
parameters in mean, scale correlation structures are estimated based on
quasi-likelihood. Multiple model selection criterion are provided for
selection of mean model and working correlation structure based on
WGEE/GEE.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
