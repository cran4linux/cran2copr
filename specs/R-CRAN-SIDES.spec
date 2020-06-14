%global packname  SIDES
%global packver   1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15
Release:          2%{?dist}
Summary:          Subgroup Identification Based on Differential Effect Search

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-nnet >= 7.3.12
BuildRequires:    R-survival >= 2.37.7
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-memoise >= 1.0.0
BuildRequires:    R-CRAN-multicool >= 0.1.9
BuildRequires:    R-MASS 
Requires:         R-nnet >= 7.3.12
Requires:         R-survival >= 2.37.7
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-memoise >= 1.0.0
Requires:         R-CRAN-multicool >= 0.1.9
Requires:         R-MASS 

%description
Provides function to apply "Subgroup Identification based on Differential
Effect Search" (SIDES) method proposed by Lipkovich et al. (2011)
<doi:10.1002/sim.4289>.

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
