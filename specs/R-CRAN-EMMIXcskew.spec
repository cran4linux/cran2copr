%global packname  EMMIXcskew
%global packver   0.9-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}
Summary:          Fitting Mixtures of CFUST Distributions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-mnormt 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Functions to fit finite mixture of multivariate canonical fundamental skew
t (FM-CFUST) distributions, random sample generation, 2D and 3D contour
plots. See Lee and McLachlan (2017) <doi:10.18637/jss.v083.i03> for more
information and examples.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
