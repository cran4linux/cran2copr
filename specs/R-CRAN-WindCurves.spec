%global packname  WindCurves
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Tool to Fit Wind Turbine Power Curves

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readbitmap 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-imputeTestbench 
Requires:         R-methods 
Requires:         R-CRAN-readbitmap 
Requires:         R-grid 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-imputeTestbench 

%description
Provides a tool to fit and compare the wind turbine power curves with
successful curve fitting techniques. Facilitates to examine and compare
the performance of a user-defined power curve fitting techniques. Also,
provide features to generate power curve discrete points from a graphical
power curves. Data on the power curves of the wind turbine from major
manufacturers are provided.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
