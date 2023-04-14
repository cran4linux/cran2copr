%global __brp_check_rpaths %{nil}
%global packname  mcmcplots
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          Create Plots from MCMC Output

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coda >= 0.17.1
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-denstrip 
Requires:         R-CRAN-coda >= 0.17.1
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-denstrip 

%description
Functions for convenient plotting and viewing of MCMC output.

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
