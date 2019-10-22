%global packname  spagmix
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Artificial Spatial and Spatiotemporal Densities on BoundedWindows

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-sparr 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-sparr 
Requires:         R-CRAN-mvtnorm 

%description
A utility package containing some simple tools to design and generate
density functions on bounded regions in space and space-time, and simulate
iid data therefrom. See Davies & Hazelton (2010) <doi:10.1002/sim.3995>
for example.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
