%global __brp_check_rpaths %{nil}
%global packname  serieslcb
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Lower Confidence Bounds for Binomial Series System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-gplots 
Requires:         R-stats 

%description
Calculate and compare lower confidence bounds for binomial series system
reliability. The R 'shiny' application, launched by the function
launch_app(), weaves together a workflow of customized simulations and
delta coverage calculations to output recommended lower confidence bound
methods.

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
