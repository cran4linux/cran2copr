%global packname  gsrsb
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Group Sequential Refined Secondary Boundary

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ldbounds 
BuildRequires:    R-CRAN-xtable 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ldbounds 
Requires:         R-CRAN-xtable 

%description
A gate-keeping procedure to test a primary and a secondary endpoint in a
group sequential design with multiple interim looks. Computations related
to group sequential primary and secondary boundaries. Refined secondary
boundaries are calculated for a gate-keeping test on a primary and a
secondary endpoint in a group sequential design with multiple interim
looks. The choices include both the standard boundaries and the boundaries
using error spending functions. Version 1.0.0 was released on April 12,
2017. See Tamhane et al. (2018), "A gatekeeping procedure to test a
primary and a secondary endpoint in a group sequential design with
multiple interim looks", Biometrics, 74(1), 40-48.

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
