%global packname  MFHD
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Functional Halfspace Depth

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-depth 
BuildRequires:    R-CRAN-depthTools 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-depth 
Requires:         R-CRAN-depthTools 
Requires:         R-CRAN-matrixStats 

%description
Multivariate functional halfspace depth and median for two-dimensional
functional data.

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
