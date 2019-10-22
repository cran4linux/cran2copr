%global packname  viewshed3d
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Compute Viewshed in 3D Terrestrial Laser Scanner Scenes ofEcosystems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-tcltk >= 3.4.4
BuildRequires:    R-utils >= 3.4.4
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-tcltk2 >= 1.2.11
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-iterators >= 1.0.10
BuildRequires:    R-CRAN-rgl >= 0.99.16
BuildRequires:    R-CRAN-VoxR >= 0.5.1
BuildRequires:    R-CRAN-viridis >= 0.5.1
Requires:         R-tcltk >= 3.4.4
Requires:         R-utils >= 3.4.4
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-tcltk2 >= 1.2.11
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-iterators >= 1.0.10
Requires:         R-CRAN-rgl >= 0.99.16
Requires:         R-CRAN-VoxR >= 0.5.1
Requires:         R-CRAN-viridis >= 0.5.1

%description
A set of tools to compute viewshed in 3D from Terrestrial Laser Scanner
data and prepare the data prior to visibility calculation.

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
