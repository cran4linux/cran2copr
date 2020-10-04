%global packname  QUALYPSO
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Partitioning Uncertainty Components of an Incomplete Ensemble ofClimate Projections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
These functions use data augmentation and Bayesian techniques for the
assessment of single-member and incomplete ensembles of climate
projections. It provides unbiased estimates of climate change responses of
all simulation chains and of all uncertainty variables. It additionally
propagates uncertainty due to missing information in the estimates. -
Evin, G., B. Hingray, J. Blanchet, N. Eckert, S. Morin, and D. Verfaillie.
(2019) <doi:10.1175/JCLI-D-18-0606.1>.

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
%{rlibdir}/%{packname}/INDEX
