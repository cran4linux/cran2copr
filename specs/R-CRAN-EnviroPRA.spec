%global __brp_check_rpaths %{nil}
%global packname  EnviroPRA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Environmental Probabilistic Risk Assessment Tools

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-truncdist 
Requires:         R-MASS 
Requires:         R-CRAN-kSamples 
Requires:         R-stats 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-truncdist 

%description
Methods to perform a Probabilistic Environmental Risk assessment from
exposure to toxic substances - i.e. USEPA (1997)
<https://www.epa.gov/risk/guiding-principles-monte-carlo-analysis> -.

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
