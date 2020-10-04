%global packname  ReacTran
%global packver   1.4.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Reactive Transport Modelling in 1d, 2d and 3d

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-shape 
Requires:         R-stats 
Requires:         R-graphics 

%description
Routines for developing models that describe reaction and
advective-diffusive transport in one, two or three dimensions. Includes
transport routines in porous media, in estuaries, and in bodies with
variable shape.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
