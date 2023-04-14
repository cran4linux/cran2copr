%global __brp_check_rpaths %{nil}
%global packname  coenoflex
%global packver   2.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Gradient-Based Coenospace Vegetation Simulator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-mgcv 
Requires:         R-mgcv 

%description
Simulates the composition of samples of vegetation according to
gradient-based vegetation theory.  Features a flexible algorithm
incorporating competition and complex multi-gradient interaction.

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
