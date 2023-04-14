%global __brp_check_rpaths %{nil}
%global packname  IsotopeR
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          3%{?dist}%{?buildtag}
Summary:          Stable Isotope Mixing Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fgui 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-fgui 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-plotrix 

%description
Estimates diet contributions from isotopic sources using JAGS. Includes
estimation of concentration dependence and measurement error.

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
