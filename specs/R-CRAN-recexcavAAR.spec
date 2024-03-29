%global __brp_check_rpaths %{nil}
%global packname  recexcavAAR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          3D Reconstruction of Archaeological Excavations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-CRAN-kriging >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-kriging >= 1.1
Requires:         R-CRAN-Rcpp >= 0.12.7

%description
A toolset for 3D reconstruction and analysis of excavations. It provides
methods to reconstruct natural and artificial surfaces based on field
measurements. This allows to spatially contextualize documented subunits
and features. Intended to be part of a 3D visualization workflow.

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
