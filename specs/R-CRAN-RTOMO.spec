%global packname  RTOMO
%global packver   1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Visualization for Seismic Tomography

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-CRAN-RPMG 
BuildRequires:    R-CRAN-GEOmap 
BuildRequires:    R-CRAN-RSEIS 
BuildRequires:    R-CRAN-splancs 
Requires:         R-CRAN-RPMG 
Requires:         R-CRAN-GEOmap 
Requires:         R-CRAN-RSEIS 
Requires:         R-CRAN-splancs 

%description
Aimed at seismic tomography, the package plots tomographic images, and
allows one to interact and query three-dimensional tomographic models.
Vertical cross-sectional cuts can be extracted by mouse click. Geographic
information can be added easily.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
